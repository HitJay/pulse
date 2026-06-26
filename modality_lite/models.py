from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class AssessmentCase:
    target: str
    intended_direction: str | None = None
    tissue_context: str | None = None


@dataclass(frozen=True)
class TargetFeatures:
    symbol: str
    ensembl_id: str | None
    approved_name: str | None
    biotype: str | None
    tractability: dict[str, set[str]] = field(default_factory=dict)
    source_url: str | None = None

    def has_tractability(self, modality: str, label: str) -> bool:
        return label in self.tractability.get(modality, set())

    def labels_for(self, modality: str) -> set[str]:
        return self.tractability.get(modality, set())

    @property
    def transcript_exists(self) -> bool:
        return self.biotype == "protein_coding" or bool(self.ensembl_id)


@dataclass(frozen=True)
class ModalityFit:
    modality: str
    fit: str
    reason: list[str]
    missing_evidence: list[str]
    evidence_fields: list[str]
    source_links: list[str]

    def as_dict(self) -> dict[str, object]:
        return {
            "modality": self.modality,
            "fit": self.fit,
            "reason": self.reason,
            "missing_evidence": self.missing_evidence,
            "evidence_fields": self.evidence_fields,
            "source_links": self.source_links,
        }


@dataclass(frozen=True)
class AssessmentResult:
    case: AssessmentCase
    target_features: TargetFeatures
    modality_fits: list[ModalityFit]

    def as_dict(self) -> dict[str, object]:
        return {
            "case": {
                "target": self.case.target,
                "intended_direction": self.case.intended_direction,
                "tissue_context": self.case.tissue_context,
            },
            "target_features": {
                "symbol": self.target_features.symbol,
                "ensembl_id": self.target_features.ensembl_id,
                "approved_name": self.target_features.approved_name,
                "biotype": self.target_features.biotype,
                "tractability": {
                    modality: sorted(labels)
                    for modality, labels in sorted(self.target_features.tractability.items())
                },
                "source_url": self.target_features.source_url,
            },
            "modality_fits": [fit.as_dict() for fit in self.modality_fits],
        }