# Monthly Report — 2026/10 (QYJI)

**Date:** 2026/10/30
**Author:** Jin Qiuye (Jay) — QYJI
**Period:** 2026-09-25 → 2026-10-30
**Format:** 2-Slide Executive Table (Page 1/2: Capability & Target Safety; Page 2/2: Structural Druggability & Assay)

---

## Page 1/2 — Capability & Target Safety

| Category | List of activities | Brief description | Relevant links/files |
|---|---|---|---|
| **Capability** | **Safety Landscape Tool — v1.4.7–v1.4.9 local Qwen baseline, Color_Basis & marketplace benchmark** | 1. Re-baselined scoring pipeline to local **qwen3.8-27b-fp8** (TP2, 16k ctx) with backend-conditional RED dual gate (**max_kw ≥ 80**) & Laya sanity gate at **T = 0.7** (**0.6492 live gate acc** on NCBN-305); tested and closed 4 optimization paths with archived A/B evidence (**v1.4.9**). <br>2. Benchmarked 3 marketplace summary backends on frozen 300-target snapshot: established **gemini_4_argon** (**0.6426 acc**, 76 min) and **kimi_k3** (**0.6426 acc**) as fallback #1/#2. <br>3. Added **Color_Basis & Color_Chain** provenance tracking (**900/900** benchmark replay equivalence), target-level `checkpoint.jsonl` resume, and **STAT3 inhibition YELLOW** gold-conflict adjudication. | [RIC-349](https://jira.novonordisk.com/browse/RIC-349) |
| | **Safety gate dry/wet consistency study — 175 HepG2 targets vs ATP & TMRM toxicity** | 1. Evaluated **175/175 RIC-381 HepG2 siRNA targets** under inhibition direction (**92 RED \| 64 YELLOW \| 19 GREEN**) on checkpointed local vLLM backend and aligned **172 targets** against wet-lab ATP, TMRM ΔΨm, and imaging toxicity readouts. <br>2. Quantified near-zero correlation across all wet endpoints (**Spearman r = -0.06 to +0.15**; strata toxic rate RED **27%** / YELLOW **33%** / GREEN **24%**), establishing expected **construct independence** (human clinical/genetic safety vs acute cellular viability). <br>3. Confirmed safety gate remains authoritative for **Red line item 5**, with **25 Non-RED & wet-toxic** cases routed for P1 calibration (**RIC-409 closed as Done**). | [RIC-409](https://jira.novonordisk.com/browse/RIC-409) / [RIC-381](https://jira.novonordisk.com/browse/RIC-381) |
| | **Proteome-wide PPI screening (RF2-PPI Science 2025) & disease-variant interface mapping** | 1. Reproduced **RF2-PPI** (Zhang et al., *Science* 2025) across all **33,000 benchmark pairs** on 6× A100 GPUs: weighted **AUCPR = 0.262** (**262×** vs 1:1000 random baseline), **20.8% recall at 90% precision** (623 pairs, 0 top-rank FP), and **43.2% recall** on large interfaces; author score parity **Pearson r = 0.919** across 8,977 pairs. <br>2. Built **interface-variants module** (`bbbkit interface-variants`, Pei et al. 2026 method; **22 unit tests passing**) mapping dual-evidence pathogenic SAVs (AlphaMissense + UniProt) onto 3D PPI interfaces (6 Å cutoff). <br>3. Delivered **1-page biology-facing proposal slide** (PPTX + @3x PNG + speaker notes) linking proteome triage to **RIC-407** GIGYF1–GRB10 glue campaign. | [RIC-410](https://jira.novonordisk.com/browse/RIC-410) / [RIC-407](https://jira.novonordisk.com/browse/RIC-407) |
| **Targets** | **Target safety pipeline — periodic rounds W40–W44 & ZHCO T2D/obesity panel (298 pairs)** | 1. Processed 4 weekly Highway/periodic rounds for YLV with 100% coverage & Color_Basis audit: **W40** (61 pairs: **24R/31Y/6G**), **W41** (63 pairs: **16R/33Y/14G**), **W42** (60 pairs: **14R/31Y/15G**), **W43** (62 pairs: **10R/43Y/9G**), and **W44** (63 pairs: **15R/35Y/13G**). <br>2. Delivered **ZHCO T2D/obesity 25-gene bidirectional panel** (**50 pairs**: 45 fresh + 5 legacy; **13 RED \| 20 YELLOW \| 17 GREEN**). <br>3. Enforced backend-aware RED dual gate in delivery verification (`check_color_basis.py`, **0 errors** across W41–W44) and refreshed PTH2R activation live row. | [RIC-391](https://jira.novonordisk.com/browse/RIC-391) |
| | **Ad-hoc target safety evaluations — FAP conjugate anchor, PROKR1, AGTR1 & APOA5** | 1. **FAP** (Apps #14, YZGC MASH/CKD/HF siRNA-conjugate anchor): **GREEN (0)** both directions; decoupled historical cell-ablation cachexia/anemia (PMID 23712428) from benign enzymatic/expression loss (*Fap* KO viable, gnomAD **pLI ≈ 0**); defined **Fc effector-silence (LALA-PG)** & sFAP sink boundaries. <br>2. **PROKR1 & AGTR1** (Apps #16–#17, EJNH T2D/obesity): PROKR1-inh **GREEN (0)**; PROKR1-act reclassified **RED → YELLOW (84)** after PubMed audit disproved hypotension claim; AGTR1-act **YELLOW (100)** (LLM downgrade; pressor/renal remodeling liabilities). <br>3. **APOA5** (App #20, EJNH T2D): fresh dual-direction run on local vLLM (**~1 min/dir**): activation **GREEN (0)**, inhibition **YELLOW (75)**. | [RIC-391](https://jira.novonordisk.com/browse/RIC-391) |

---

## Page 2/2 — Structural Druggability & Assay

| Category | List of activities | Brief description | Relevant links/files |
|---|---|---|---|
| **Targets** | **TSPO ligands (PK11195, emapunil, etifoxine, FGIN-1-27, alpidem) — target deconvolution & FEP** | 1. Multi-layer off-target deconvolution across 5 ligands (ChEMBL/PubChem + GTEx + OpenTargets + 17-pocket Vina gate + SwissTargetPrediction + **Boltz-2 de novo co-folding**): proved **CAR (NR1I3) is the dominant metabolic target of PK11195** (IC50 **25–56 nM**, confirmed by **5 independent method families**, Boltz-2 CAR-LBD centroid **2.52 Å** from crystal agonist). <br>2. Exposure-occupancy gate: **emapunil** selectively engages TSPO (**13.5% occ** at 90 mg qd, Ki 6.4 nM); **etifoxine** (**<0.01% occ**, Ki 7.8 µM) & **alpidem** fail TSPO occupancy at clinical exposure (alpidem acts via GABA-A BZD site). <br>3. Completed **250 ps restrained MD** + **annihilation alanine-scanning TI (21 anchors)** across known & fpocket novel pockets (identifying TSPO dimer pocket `4RYI_p26` LEU58 & GABA-A `6X3X_p78` SER196); delivered self-contained HTML reports, 1920×1080 one-pager, and **7-slide EN/CN decks** to ZHCO/ZC. | [RIC-408](https://jira.novonordisk.com/browse/RIC-408) |
| **Assay** | **IGWU myotube atrophy — zero-shot foundation model benchmark & ACVR / GRB10 batch readouts** | 1. **Zero-shot foundation model benchmark** across **720 wells** (3 IGWU batches): evaluated Google **EmbeddingGemma-2** (740M), Meta **SAM 2.1**, and **SAM 3** (848M) against v3.5 decoupled CellProfiler. Embedding variance is dominated by batch (**η² = 0.12–0.36** vs condition **~0.04**; within-batch kNN lift collapses to **1.1×**); SAM 2.1/3 over-segment inter-fibre background (**IoU = 0.412 / 0.408** vs CP mask) — all 3 rejected zero-shot, confirming **CellProfiler combination_mask** as authoritative. <br>2. Onboarded **IGWU_20260923_1** (ACVR factorial, **240/240 wells**: ALK4/ALK5 inhibitors increase length **+17.0% to +17.9%**, **+1.27 SSMD**) and **IGWU_20260923_2** (GRB10 siRNA, **240/240 wells**: GRB10 neutral, IGFBP5 KD **-11.5% length**); fixed CIFS concurrent hardlink lock via `copyfile`. | [RIC-261](https://jira.novonordisk.com/browse/RIC-261) / [RIC-394](https://jira.novonordisk.com/browse/RIC-394) |
| | **Seahorse assay imaging pipeline — PR #2 multi-lineage 900-well benchmark & BP portal release** | 1. Executed full generalization benchmark of **PR #2** (per-well rim & pillar detection engine, co-developed with AXVN) across the **15-batch production panel** (**900 wells, 7,200 fields**) spanning **Mature Adipocytes, Skeletal Muscle, and HepG2**. <br>2. Confirmed **1.0–2.0 px median pillar residual** (eliminating legacy 6–7 px rigid offset) with zero parameter retuning; unmasked **+4.45% cell count** on 3D adipocytes (recovering a previously hidden knockdown respiration gain) and verified automatic fallback on a 35–60 px stage-shifted plate (**-0.63% delta**). <br>3. Updated **Gen 2.2 Best Practice summary** (§11.5) with automated confidentiality/vendor leakage assertions for standalone portal publishing. | [RIC-375](https://jira.novonordisk.com/browse/RIC-375) |
| **Capability** | **RIC portfolio review (2026 Goals / Highway alignment) & legacy ticket hygiene closeout** | 1. Completed **RIC Portfolio Review v2.4** aligning all active tickets and FTE allocation against **2026 Goals (G1–G8)** and the **NNRCC Highway / Red line operational model** (6 MOA clusters, stop/go de-risking narrative). <br>2. Executed structured **Closure sub-variant workflow** (Description posterity rewrite + timeline/outcome table + Done gate fields + assignee verification) across **14 completed or superseded legacy tickets** (**RIC-247** decoupled pipeline umbrella, **RIC-298** adipocyte lipolysis vAssay, **RIC-358** EE TMRM support, plus 11 completed assay/campaign cards on Oct 15). | [RIC-247](https://jira.novonordisk.com/browse/RIC-247) / [RIC-298](https://jira.novonordisk.com/browse/RIC-298) / [RIC-358](https://jira.novonordisk.com/browse/RIC-358) |

---

## Tickets in period

**New / Activated**
- RIC-410 — RF2-PPI (Zhang Science 2025) method reproduction + interface disease-variant mapping capability
- RIC-409 — Dry/wet consistency check: safety gate (175 RIC-381 HepG2 targets) vs ATP/TMRM toxicity signals (opened & closed as Done)
- RIC-408 — TSPO ligands (PK11195, emapunil/XBD173, etifoxine, FGIN-1-27, alpidem) target search & FEP validation for Group 3 proposal

**Progressed**
- RIC-349 (v1.4.7–v1.4.9 local qwen3.8-27b-fp8 baseline, backend-aware dual gate, marketplace 3-model benchmark, Color_Basis provenance, STAT3 adjudication)
- RIC-391 (Applications #14 FAP, #15 W41/W42/ZHCO 50-pair panel, #16 PROKR1, #17 AGTR1, #18 W43, #19 W44, #20 APOA5)
- RIC-261 (Zero-shot foundation model evaluation: EmbeddingGemma-2, SAM 2.1, SAM 3 vs CellProfiler across 720 wells)
- RIC-394 (IGWU_20260923_1 ACVR factorial & IGWU_20260923_2 GRB10 siRNA batch onboarding + CIFS copyfile fix)
- RIC-375 (PR #2 per-well rim/pillar engine 15-batch / 900-well multi-lineage benchmark & Gen 2.2 BP portal hardening)
- RIC-407 (Cross-linked RF2-PPI 33k-pair calibration & interface-variants module for GIGYF1–GRB10 lead triage)

**Closed / Done**
- RIC-409 — Dry/wet consistency check on 175 HepG2 targets (Done 2026-10-16)
- RIC-247 / RIC-298 / RIC-358 — Umbrella & campaign support tickets formally closed with full activity logs (Done 2026-10-27)
- Portfolio hygiene pass (2026-10-15): RIC-292, RIC-217, RIC-209, RIC-254, RIC-384, RIC-392, RIC-331, RIC-270, RIC-262, RIC-218, RIC-246, RIC-245, RIC-244 closed as Done

**In Review**
- RIC-393 (GHSR inverse agonist docking), RIC-405 (siGRB10 off-targets), RIC-400 (PEX16 negation fix)
