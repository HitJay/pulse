# Monthly Report — 2026/09 (QYJI)

**Date:** 2026/09/25
**Author:** Jin Qiuye (Jay) — QYJI
**Period:** 2026-08-28 → 2026-09-25
**Format:** 2-Slide Executive Table (Page 1/2: Capability & Target Safety; Page 2/2: Structural Druggability & Assay)

---

## Page 1/2 — Capability & Target Safety

| Category | List of activities | Brief description | Relevant links/files |
|---|---|---|---|
| **Capability** | **Safety Landscape Tool — archive re-platforming & v1.4.4 gateway hardening** | 1. Re-platformed all 281 v1.x legacy archive rows onto **v1.4.3 live pipeline rows** across 8 chunks + c9/c10 top-ups (**297 pairs re-assessed**, 0 failures); every row now carries keyword-level evidence; report links on **862/863 rows**; **RIC-398 closed as Done**. <br>2. Engine & gateway hardening (v1.4.4): resolved Azure LiteLLM HTTP 400 gateway rejection on `temperature=0.0` for Opus 5; disabled reasoning token overflow; expanded negation vocabulary (**avoiding** / **risk is low**) to eliminate false-positive REDs (PRR5). <br>3. IT lifecycle management: completed system management & IT risk documentation package for Q187219 review (**RIC-404**). | [RIC-349](https://jira.novonordisk.com/browse/RIC-349) / [RIC-398](https://jira.novonordisk.com/browse/RIC-398) / [RIC-404](https://jira.novonordisk.com/browse/RIC-404) |
| | **Safety Landscape Tool — Dashboard Score & Keywords columns, search expansion** | 1. Dashboard table enhanced with dedicated **Score** (numerical ascending/descending sort) and **Matched Keywords** columns displaying quantitative weights and toxicological risk tags. <br>2. Global search filter expanded to support **toxicity keywords** (e.g. *pancreatitis*, *seizure*, *lactic acidosis*), exact scores, and colleague requester initials (**zhco, ylv, ejnh**); updated search placeholder. <br>3. Enforced **direction-matched NCBN gold labels** to eliminate cross-direction attribution overrides (ACOX1, ACACA, MEN1, NLRP3). | [RIC-395](https://jira.novonordisk.com/browse/RIC-395) |
| | **Druggability Agent — v0.2.0 platform architecture & peptide engineering framework** | 1. Codebase elevated to top-level **druggability namespace (v0.2.0)**, retaining bbbkit backward-compatibility shim; all **156 unit tests passing**; codified persistent Agent skill `peptide-druggability-assessment`. <br>2. Multi-tier peptide engineering toolset deployed: Layer 1 **PRODIGY contact affinity** (ΔG / Kd); Layer 2 in silico Alanine scanning & 20-AA mutational matrix; Layer 3 GPU short-MD ensemble MM/GBSA (**>2,100 ns/day on A100**) resolving static void artifacts; Layer 4 subtype selectivity audit. <br>3. Standardized **DrugCLIP contrastive AI screening** (NeurIPS 2023) on A100 for automated pocket extraction and sub-second chemical library retrieval. | [RIC-403](https://jira.novonordisk.com/browse/RIC-403) |
| **Targets** | **Target safety pipeline — periodic round W38, individual requests & PEX16 fix** | 1. Application #12 (W38 periodic round for YLV): 47 unique pairs evaluated: **18 RED \| 13 YELLOW \| 16 GREEN**; ANXA5 dual-direction evaluated (Act YELLOW 72 / Inh GREEN 0); 100% programmatic coverage audit. <br>2. Application #9 & #11: GPR68 inhibition (**GREEN 0**, CCEG) and PIKFYVE inhibition (**RED 126**, ZHCO; human clinical exposure review of apilimod). <br>3. PEX16 negation mis-suppression resolved (**RIC-400**): HGNC alias expansion in PubMed query; MUL1 re-run and post-delivery evidence addendum on murine HCC liability (PMID 37962001). | [RIC-391](https://jira.novonordisk.com/browse/RIC-391) / [RIC-400](https://jira.novonordisk.com/browse/RIC-400) |
| | **siGRB10 off-target safety evaluation — PRR5, LTN1, ALKBH8, LRRCC1 (liver focus)** | 1. Liver-focused in vivo tolerability evaluation of 4 off-target candidates under inhibition direction: **3 YELLOW** (PRR5, LTN1, ALKBH8) \| **1 GREEN** (LRRCC1); completed in **~4.5 min end-to-end** (~1.1 min/target). <br>2. PRR5 root-cause diagnosis: resolved false-positive RED via negative-context negation fix (**Score 44 YELLOW**; selective KO avoids Rictor/mTOR lethality; gnomAD pLI ≈ 0). <br>3. Delivered 7-slide executive Marp deck (`.pptx` + `.html`) with clinical/genetic liabilities and monitoring recommendations to requester YLV. | [RIC-405](https://jira.novonordisk.com/browse/RIC-405) |

---

## Page 2/2 — Structural Druggability & Assay

| Category | List of activities | Brief description | Relevant links/files |
|---|---|---|---|
| **Targets** | **GPR81 (HCAR1) target assessment — orthosteric vs allosteric modes & OpenFEP** | 1. Receptor structural alignment (human 8Z8A vs cryo-EM HCAR2 8J6P): lactate/niacin orthosteric centers superimpose within 0.75 Å; maps allosteric agonist to TM5-TM6-ECL2 crevice (**17.7 Å separation**); corroborated by ebBRET literature establishing Agonist 1 as **ago-PAM** vs AZ1/AZ7136 as **orthosteric agonists**. <br>2. Completed converged **congeneric OpenFEP simulation** across all 3 legs (constrained pyridones lead c28/c26/c30/c38 vs AZ series). <br>3. Delivered **14-slide executive presentation deck** (pptx/pdf), interactive 3D WebGL report, and paste-ready readout email to colleague Huan (UHYG). | [RIC-396](https://jira.novonordisk.com/browse/RIC-396) |
| | **GIGYF1–GRB10/14–INSR axis — clinical genetics perturbation & molecular glue audit** | 1. In silico clinical genetics perturbation on 1.79 Å GIGYF1:GRB10 complex: identified **p.Tyr498Cys with massive ΔΔG = +2.74 kcal/mol** (>80-fold affinity loss), directly validating GIGYF1-GRB10 disruption as causal driver of T2D predisposition in humans (**OR = 5.91**); p.Trp494Arg (+1.80 kcal/mol) and p.Ser474Ter (+5.88 kcal/mol). <br>2. A100 GPU explicit-solvent MD (1,103 solute atoms in TIP3P): backbone RMSD converged at **0.36 ± 0.08 Å**; identified Pro1 (-50.4 kcal/mol) and Leu4 (-40.0 kcal/mol) as core anchors. <br>3. Delivered **8-slide executive Marp deck** (pptx/pdf) with Tier 0 in silico virtual screening recommendations for JXDL. | [RIC-407](https://jira.novonordisk.com/browse/RIC-407) |
| | **OXTR individual target assessment — structural pharmacology & subtype selectivity** | 1. Structural pharmacology & selectivity audit across human active (7QVM/7RYC) vs inactive (6TPK) OXTR, and subtype counter-screen with vasopressin V2R (7DW9). <br>2. Pro7Gly selectivity mechanism: V2R 3.51 Å Helix I constriction + ECL3 Leu302 hydrophobic mismatch causes severe steric clash on V2R while OXTR accommodates Gly7. <br>3. Confirmed Leu8 as solvent-exposed exit vector for fatty-acid acylation (Lys8 substitution favorable at **-12.16 kcal/mol** with unobstructed 3D conical clearance, rationalizing Lilly long-acting design); delivered standalone 3Dmol.js HTML dossiers. | [RIC-403](https://jira.novonordisk.com/browse/RIC-403) |
| **Assay** | **IGWU myotube — MEK inhibitor factorial & IGF/Insulin dose-response repeat** | 1. IGWU_20260907_1 (MEK Inhibitor Factorial): U0126/PD98059 × dose (0.16–20 µM) × IGF ligand plate onboarded on decoupled v3.5 pipeline (**240/240 wells**); identified phenotypic split at 20 µM: negative nuclei count alongside peaked morphological hypertrophy (length **+1.52 SSMD**, fusion index **+1.75 SSMD**). <br>2. IGWU_20260907_2 (IGF/Insulin Dose-Response Repeat): 240 wells processed; confirmed consistent negative length dose-response across all three ligands (-5% to -14%, strongest IGF2 **-1.52 SSMD** at 4 nM) with counter-directional MYH intensity elevation (IGF2_1000 **+3.06 SSMD**) reflecting differentiation remodeling. | [RIC-394](https://jira.novonordisk.com/browse/RIC-394) |
| | **Seahorse assay imaging pipeline — Production Baseline Gen 2.2 release** | 1. Released **Production Baseline Gen 2.2** (Multi-scale LoG + Per-Well Kasa Circle Refitting + Soft-Edge Profile + Rigid Pillar Dynamics) across 5x Seahorse automated counting. <br>2. Engineering enhancements: Per-well Kasa circle refit resolves translation offsets (systematic **dx = -66.5 px** rigid shift on SkM) preventing rim eccentricity and tissue clipping; synchronized consensus pillar coordinates; radial profile soft-edge expansion (r = 795 px Adipo, 805 px SkM, 815–845 px HepG2). <br>3. Slide 4 microscopic gallery overhaul: expanded 4-column microscopic image strip (**+16.2% width**) with absolute coordinate grid stabilization for publication-grade PPTX/PDF rendering. | [RIC-375](https://jira.novonordisk.com/browse/RIC-375) |

---

## Tickets in period

**New / Activated**
- RIC-407 — GIGYF1–GRB10/14–INSR axis (PPI screening & molecular glue structural druggability)
- RIC-403 — OXTR individual target assessment (structural pharmacology & peptide engineering toolset)
- RIC-405 — siGRB10 off-target safety evaluation (PRR5, LTN1, ALKBH8, LRRCC1; liver focus)
- RIC-404 — Safety Landscape Tool lifecycle management and RI portal documentation (Q187219)
- RIC-400 — PEX16 negation mis-suppression & PubMed alias expansion

**Progressed**
- RIC-349 (v1.4.4 gateway hardening, temperature=1.0 / thinking=disabled, negation expansion)
- RIC-395 (Dashboard Score & Matched Keywords columns, toxicity keyword & initial search)
- RIC-391 (Applications #9, #11, #12 W38 round 47 pairs, #13 siGRB10 off-targets)
- RIC-396 (GPR81 orthosteric vs allosteric binding modes, congeneric OpenFEP, 14-slide deck)
- RIC-394 (IGWU_20260907_1 MEK inhibitor factorial & IGWU_20260907_2 IGF/Insulin dose-response repeat)
- RIC-375 (Seahorse imaging Production Baseline Gen 2.2 release & Slide 4 visual overhaul)

**Closed / Done**
- RIC-398 — Archive refresh campaign complete (297 pairs re-assessed, 0 legacy archive rows)
- RIC-385 — Historical safety report retrieval tool (ACOX1 backfill & direction attribution closed)
- RIC-380 — External Innovation (inactive stub closed)

**In Review**
- RIC-392 / RIC-393 — GHSR inverse agonist docking campaign (carried in Review)
