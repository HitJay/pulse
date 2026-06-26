import unittest

from modality_lite.models import AssessmentCase, TargetFeatures
from modality_lite.scoring import assess_modalities


class ModalityLiteScoringTests(unittest.TestCase):
    def test_secreted_target_fits_antibody_and_not_protac(self):
        features = TargetFeatures(
            symbol="PCSK9",
            ensembl_id="ENSG00000169174",
            approved_name="proprotein convertase subtilisin/kexin type 9",
            biotype="protein_coding",
            tractability={"AB": {"UniProt loc high conf"}, "PR": {"Small Molecule Binder"}},
        )
        fits = {fit.modality: fit for fit in assess_modalities(AssessmentCase("PCSK9", "inhibit", "liver"), features)}
        self.assertEqual(fits["antibody_biologic"].fit, "fit")
        self.assertEqual(fits["protac_degrader"].fit, "no_fit")

    def test_liver_knockdown_fits_rna_oligo(self):
        features = TargetFeatures(
            symbol="APOC3",
            ensembl_id="ENSG00000110245",
            approved_name="apolipoprotein C3",
            biotype="protein_coding",
            tractability={},
        )
        fits = {fit.modality: fit for fit in assess_modalities(AssessmentCase("APOC3", "knockdown", "liver"), features)}
        self.assertEqual(fits["rna_oligo"].fit, "fit")

    def test_small_molecule_signal_fits_small_molecule(self):
        features = TargetFeatures(
            symbol="HMGCR",
            ensembl_id="ENSG00000113161",
            approved_name="3-hydroxy-3-methylglutaryl-CoA reductase",
            biotype="protein_coding",
            tractability={"SM": {"Approved Drug", "Structure with Ligand"}},
        )
        fits = {fit.modality: fit for fit in assess_modalities(AssessmentCase("HMGCR", "inhibit", "liver"), features)}
        self.assertEqual(fits["small_molecule"].fit, "fit")


if __name__ == "__main__":
    unittest.main()