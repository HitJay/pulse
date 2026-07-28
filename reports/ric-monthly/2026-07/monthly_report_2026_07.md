# Monthly Report — 2026/07 (QYJI)

**Date:** 2026/07/31
**Author:** Jin Qiuye (Jay) — QYJI
**Period:** 2026-06-26 → 2026-07-27

---

| Category | List of activities | Brief description | Relevant links/files |
|---|---|---|---|
| **Capability** | **Safety Landscape Tool — colleague self-service intake app** | 1. New **Dashboard**: merges static archive index (**2,739 targets**, 2026-07-06 snapshot) with live cron-run registries — colleagues self-check "has this target been assessed?" before filing a request. <br>2. Fixed a Dashboard render bug (`jsonlite::validate()` masking `shiny::validate()`). <br>3. Field simplification: retired High-precision/High-recall assessment types, kept only **Standard** (0.7082 binary accuracy); removed Assessment-type/Delivery-format dropdowns; merged name field into single 2–5 letter initial. <br>4. Added one-at-a-time target entry + CSV bulk-add. Live on Posit Connect, **v1.2+35**. | [RIC-395](https://jira.novonordisk.com/browse/RIC-395) |
| | **Safety Landscape Tool — conservative RED operating point + science deep-dive + upstream alignment** | 1. **Default scoring switched to conservative RED call**: score≥75 AND max_weight≥60 → RED; reproduced NCBN-305 gold-standard benchmark: binary accuracy **0.7082**, RED precision 0.6814, RED recall 0.5923. <br>2. **34-slide science-meeting deep dive** (EN+CN): pipeline architecture, 8 data sources, keyword tuning history (P1→v5_final, Macro F1 0.381→0.498), ~70% accuracy ceiling confirmed via 4 independent CV methods. <br>3. **Benchmarked against Novo's in-house GHE safety-landscape-tool** (v0.91): ran non-blocked unit tests (32/35 pass), identified 3 environment blockers, then ported keyword-scoring + dual-gate + NCBN-305 regression suite into the upstream repo. <br>4. request_form **v1.2** live on Posit Connect: two-step submit with CSV/CLI preview, required direction field (guards a prior silent-default bug), third **High-precision** operating point added. | [RIC-349](https://jira.novonordisk.com/browse/RIC-349) / [RIC-364](https://jira.novonordisk.com/browse/RIC-364) |
| | **HepG2 EE — cross-modal model characterization** | Extended last month's cross-modal MoA story into a **model characterization** package: DRUG-seq framed as target-perturbation coordinate system, TMRM/MitoTracker as mitochondrial functional readout, DINOv2 C24/C1 as image-derived state representation, pathway score as an interpretable summary layer (not a replacement for full signature). Delivered pathway-vs-phenotype consistency analysis, tox-prediction benchmark scripts, and a one-pager. | [RIC-381](https://jira.novonordisk.com/browse/RIC-381) |
| **Targets** | **Target safety assessment applications — SAM68 / HQGH 5-target batch** | 1. **SAM68 (KHDRBS1)** (req. SIWZ, T2D): both directions **YELLOW** (activation 67 / inhibition 77) — oncogenic splicing risk vs fertility/dyslipidemia signals; neither crosses RED. <br>2. **HQGH batch** (5 targets, inhibition-only): BAIAP3 RED(82), KCNK16 YELLOW(52), P2RY1 RED(75), PKD1 RED(124, human ADPKD gene), TFRC RED(132, pLI 0.98 LoF-intolerant). | [RIC-391](https://jira.novonordisk.com/browse/RIC-391) |
| | **GHSR inverse-agonist docking campaign — virtual screening + Boltz-2 cross-validation** | 1. Dual-receptor protocol: primary dock vs inactive-state 7F83, counter-screen vs active-state 8JSR, **7,931 ChEMBL** drug/lead-like compounds, 7,930/7,931 completed. <br>2. Classification: **3,325 strong** inverse-agonist candidates (Δ<−1.0), 2,268 moderate, 1,021 pan-state binders. <br>3. **Top 50 cross-validated with Boltz-2** affinity prediction (50/50 done); top candidates AMINOQUINURIDE, MITOQUIDONE, ULECACICLIB. <br>4. Follow-up top-20 ChEMBL cross-check + liability screen scripts added. | [RIC-392](https://jira.novonordisk.com/browse/RIC-392) |
| **Assay** | **IGWU myotube atrophy — batch application log** (methodology BP v2.0.0 on RIC-261 in Review closeout) | 1. **IGWU_20260602_1 relabel + full rerun**: biology team corrected 20-well plate layout (positive-control fix); only cell_analysis+readout rerun (CellProfiler/skeleton untouched) — surfaced SB431542 as a new strong hit (FiberWidth SSMD +2.23). <br>2. Onboarded new batch series **IGWU_20260712** (Mid/Low/High dose) into the registry. <br>3. Ongoing cross-batch dashboard maintenance (dynamic STATS_CSV picker, renamed to `multi_batch_screening_dashboard`). | [RIC-394](https://jira.novonordisk.com/browse/RIC-394) / [RIC-261](https://jira.novonordisk.com/browse/RIC-261) |

---

## Tickets in period

**New**
- RIC-395 — Safety Landscape intake Shiny app (split from RIC-349)
- RIC-392 — GHSR inverse agonist docking campaign
- RIC-391 — Safety pipeline application log (opened 2026-07-13, active this period)
- RIC-394 — IGWU myotube atrophy batch application log

**Progressed**
- RIC-349 (Safety landscape tool — conservative operating point + upstream port), RIC-364 (keyword methodology deck), RIC-381 (HepG2 EE model characterization)

**In Review / closeout**
- RIC-261 (Skeletal Muscle Atrophy — v2.0.0 BP, moved to Review 2026-07-20)

**No activity this period (carried, not reported as progress)**
- RIC-390 (Lipolysis imaging), RIC-298 (Lipolysis parent), RIC-386 (DGKQ family) — no Jira comments or repo commits since 2026-06-08/2026-06-26.

---

## Deliverables

- **PPTX (single-page table):** `/das/user/QYJI/pulse/reports/ric-monthly/2026-07/monthly_report_2026_07.pptx`
- **Legacy mirror:** `/das/user/QYJI/druggability/docs/monthly_report_2026_07.pptx`
- **Shared drive mirror:** `/TDE_TV/shared_folder/QYJI/monthly_report/QYJI_2026-07-31/monthly_report_2026_07.pptx`
- **Builder script:** `/das/user/QYJI/pulse/scripts/ric-monthly/build_ric_monthly_2026_07.py`
