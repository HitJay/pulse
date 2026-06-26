from __future__ import annotations

from modality_lite.models import AssessmentCase, ModalityFit, TargetFeatures


KNOCKDOWN_DIRECTIONS = {"knockdown", "inhibit", "splice_modulate", "degrade"}
ACTIVATION_DIRECTIONS = {"activate", "agonize", "replace"}
LOCAL_OR_ESTABLISHED_OLIGO_TISSUES = {"liver", "cns_local", "eye_local", "local_delivery"}
EXTRAHEPATIC_UNCERTAIN_TISSUES = {"adipose", "skeletal_muscle", "muscle", "beta_cell", "systemic_extrahepatic"}

SM_FIT_LABELS = {
    "Approved Drug",
    "Advanced Clinical",
    "Phase 1 Clinical",
    "Structure with Ligand",
    "High-Quality Ligand",
    "High-Quality Pocket",
    "Med-Quality Pocket",
    "Druggable Family",
}
SM_BINDER_LABELS = {"High-Quality Ligand", "Structure with Ligand"}
AB_HIGH_LABELS = {"Approved Drug", "Advanced Clinical", "Phase 1 Clinical", "UniProt loc high conf", "GO CC high conf", "Human Protein Atlas loc"}
AB_MEDIUM_LABELS = {"UniProt loc med conf", "GO CC med conf", "UniProt SigP or TMHMM"}
PROTAC_SUPPORT_LABELS = {"Literature", "UniProt Ubiquitination", "Database Ubiquitination", "Half-life Data", "Small Molecule Binder"}


def assess_modalities(case: AssessmentCase, features: TargetFeatures) -> list[ModalityFit]:
    return [
        assess_small_molecule(features),
        assess_antibody(features),
        assess_rna_oligo(case, features),
        assess_protac(case, features),
        assess_peptide_fusion(case, features),
    ]


def _source_links(features: TargetFeatures) -> list[str]:
    return [features.source_url] if features.source_url else []


def _evidence(modality: str, features: TargetFeatures, labels: set[str] | None = None) -> list[str]:
    labels = labels if labels is not None else features.labels_for(modality)
    return [f"OpenTargets tractability {modality}: {label}" for label in sorted(labels)]


def _has_ab_accessibility(features: TargetFeatures) -> bool:
    return bool(features.labels_for("AB") & (AB_HIGH_LABELS | AB_MEDIUM_LABELS))


def _has_sm_binder(features: TargetFeatures) -> bool:
    return bool(features.labels_for("SM") & SM_BINDER_LABELS) or features.has_tractability("PR", "Small Molecule Binder")


def assess_small_molecule(features: TargetFeatures) -> ModalityFit:
    supporting = features.labels_for("SM") & SM_FIT_LABELS
    if supporting:
        fit = "fit"
        reason = ["Small-molecule precedent or tractability signal is present."]
        missing = ["Selectivity, assay quality, and ADMET are not assessed in MVP."]
    else:
        fit = "weak"
        reason = ["No OpenTargets small-molecule ligand, pocket, structure, family, or clinical signal was found."]
        missing = ["Need ligand, pocket, structure, family, or clinical small-molecule evidence."]
    return ModalityFit("small_molecule", fit, reason, missing, _evidence("SM", features, supporting), _source_links(features))


def assess_antibody(features: TargetFeatures) -> ModalityFit:
    high = features.labels_for("AB") & AB_HIGH_LABELS
    medium = features.labels_for("AB") & AB_MEDIUM_LABELS
    if high:
        fit = "fit"
        reason = ["High-confidence antibody/biologic accessibility or clinical biologic signal is present."]
        missing = ["Epitope, species cross-reactivity, and developability are not assessed in MVP."]
        evidence = high
    elif medium:
        fit = "possible"
        reason = ["Medium-confidence extracellular, membrane, signal peptide, or transmembrane evidence is present."]
        missing = ["Need higher-confidence localization or biologic precedent."]
        evidence = medium
    else:
        fit = "unknown"
        reason = ["No antibody accessibility signal was found in OpenTargets tractability."]
        missing = ["Need secreted, extracellular, plasma-membrane, or biologic precedent evidence."]
        evidence = set()
    return ModalityFit("antibody_biologic", fit, reason, missing, _evidence("AB", features, evidence), _source_links(features))


def assess_rna_oligo(case: AssessmentCase, features: TargetFeatures) -> ModalityFit:
    direction = (case.intended_direction or "").lower()
    tissue = (case.tissue_context or "").lower()
    if direction in ACTIVATION_DIRECTIONS:
        return ModalityFit(
            "rna_oligo",
            "no_fit",
            ["RNA/oligo MVP rules mainly support knockdown or splice modulation, not activation or replacement."],
            ["Use peptide/fusion or agonist modality if activation/replacement is desired."],
            [],
            _source_links(features),
        )
    if direction and direction not in KNOCKDOWN_DIRECTIONS:
        return ModalityFit(
            "rna_oligo",
            "unknown",
            ["The intended direction is not mapped to an RNA/oligo rule."],
            ["Specify knockdown, inhibit, or splice_modulate if RNA-level intervention is intended."],
            [],
            _source_links(features),
        )
    if not direction:
        return ModalityFit(
            "rna_oligo",
            "unknown",
            ["RNA/oligo fit depends strongly on intended direction, which was not provided."],
            ["Specify intended_direction such as knockdown or splice_modulate."],
            [f"Target biotype: {features.biotype or 'unknown'}"],
            _source_links(features),
        )
    if not features.transcript_exists:
        return ModalityFit("rna_oligo", "no_fit", ["No transcript-level target evidence was available."], ["Resolve target transcript identity."], [], _source_links(features))

    if tissue in LOCAL_OR_ESTABLISHED_OLIGO_TISSUES:
        fit = "fit"
        reason = ["Knockdown/splice direction matches RNA-level intervention and tissue context has a plausible MVP delivery route."]
        missing = ["Sequence design, off-target, chemistry, and dose window are not assessed in MVP."]
    elif tissue in EXTRAHEPATIC_UNCERTAIN_TISSUES:
        fit = "weak"
        reason = ["Knockdown/splice direction matches RNA-level intervention, but systemic extrahepatic delivery is uncertain in MVP rules."]
        missing = ["Need delivery strategy for this tissue context."]
    else:
        fit = "possible"
        reason = ["Knockdown/splice direction matches RNA-level intervention, but tissue delivery context is missing or not classified."]
        missing = ["Specify tissue_context or provide delivery evidence."]
    return ModalityFit("rna_oligo", fit, reason, missing, [f"Target biotype: {features.biotype or 'unknown'}"], _source_links(features))


def assess_protac(case: AssessmentCase, features: TargetFeatures) -> ModalityFit:
    direction = (case.intended_direction or "").lower()
    protac_labels = features.labels_for("PR") & PROTAC_SUPPORT_LABELS
    sm_binder = _has_sm_binder(features)
    accessible_to_antibody = _has_ab_accessibility(features)

    if accessible_to_antibody:
        return ModalityFit(
            "protac_degrader",
            "no_fit",
            ["Target has extracellular/biologic accessibility signals, so classic intracellular PROTAC fit is poor in MVP rules."],
            ["Need intracellular target-product evidence and binder evidence for degrader hypothesis."],
            _evidence("AB", features) + _evidence("PR", features, protac_labels),
            _source_links(features),
        )
    if sm_binder and (not direction or direction in KNOCKDOWN_DIRECTIONS):
        fit = "possible" if not direction else "fit"
        reason = ["Small-molecule binder or PROTAC support signal is present; degrader may be plausible if target product is intracellular."]
        missing = ["Need intracellular localization, degradation advantage, E3 context, and degradation assay evidence."]
    else:
        fit = "weak"
        reason = ["No small-molecule binder or PROTAC support signal was found."]
        missing = ["Need binder and intracellular target-product evidence."]
    return ModalityFit("protac_degrader", fit, reason, missing, _evidence("PR", features, protac_labels) + _evidence("SM", features, features.labels_for("SM") & SM_BINDER_LABELS), _source_links(features))


def assess_peptide_fusion(case: AssessmentCase, features: TargetFeatures) -> ModalityFit:
    direction = (case.intended_direction or "").lower()
    ab_accessibility = _has_ab_accessibility(features)
    if direction in {"agonize", "antagonize", "replace", "ligand_trap", "fusion"}:
        fit = "possible"
        reason = ["The intended direction is compatible with peptide, fusion, replacement, or ligand-trap logic."]
        missing = ["Need receptor/ligand biology, construct design, half-life, and safety-window evidence."]
    elif ab_accessibility:
        fit = "possible"
        reason = ["Target has extracellular or secreted accessibility signals, so peptide/fusion or ligand-trap concepts may be worth checking."]
        missing = ["Need explicit ligand/receptor or replacement mechanism."]
    else:
        fit = "unknown"
        reason = ["No peptide/fusion-specific rule was triggered in MVP." ]
        missing = ["Need target class, ligand/receptor axis, or intended fusion/replacement mechanism." ]
    return ModalityFit("peptide_fusion", fit, reason, missing, _evidence("AB", features) if ab_accessibility else [], _source_links(features))