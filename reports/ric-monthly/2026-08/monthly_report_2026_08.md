# Monthly Report — 2026/08 (QYJI)

**Date:** 2026/08/28
**Author:** Jin Qiuye (Jay) — QYJI
**Period:** 2026-07-28 → 2026-08-27

---

| Category | List of activities | Brief description | Relevant links/files |
|---|---|---|---|
| **Capability** | **Safety Landscape Tool — v1.4 MoA biology layer + operations hardening** | 1. New **Mechanism-of-Action biology layer** on OpenTargets v4: pathways, drug MoA, probes, subcellular location; completed the action-type vocabulary from a live OT probe (BLOCKER/OPENER/POSITIVE MODULATOR…), direction-neutral terms stay silent. <br>2. Rendered as "MoA Profile" section in md/marp/pptx outputs; NCBN-305 gold-standard gate re-run: **Δacc = 0** (scoring untouched). <br>3. Gold-standard direction-provenance fix (HMGB1 request trigger) + snapshot-consistency audit. <br>4. Model alias migrated opus_latest → **opus_5_azure** for unambiguous audit traces. | [RIC-349](https://jira.novonordisk.com/browse/RIC-349) |
| | **Safety Landscape Tool — colleague self-service adoption + Dashboard updates** | 1. Self-service intake app adopted by colleagues: **10 submitted requests in August** (ZHCO, ZYGS, EJNH, YLV, SIWZ), incl. multi-target batches and MASH variants. <br>2. Dashboard: added **Requester column** (fallback "not know") and "Last 24 hours" time filter. <br>3. Pre-check flows now flag archive-snapshot-only targets before filing. | [RIC-395](https://jira.novonordisk.com/browse/RIC-395) |
| | **Imaging best practice — BP poster iteration** | Per leadership feedback the poster narrative was shifted from two case studies to *general imaging best practice* (7-stage workflow + data flow), with assays demoted to proof-of-concept evidence; iterated to **v49** through 6 review rounds. | [RIC-379](https://jira.novonordisk.com/browse/RIC-379) |
| **Targets** | **GPR81 (HCAR1) individual target assessment — docking, reverse-SAR & safety** | 1. Three-layer deliverable to requester UHYG: **Vina docking | Boltz-2 | wet-lab benchmark**, **45/45 compounds** covered at every layer; full-chain data-integrity audit (20 checks, all pass). <br>2. New finding — binding-site disagreement between layers: Boltz-2 places **29/45 compounds in the orthosteric pocket contacting Arg71** (lactate carboxylate anchor); Vina on experimental structures disagrees → report section 7 + site-disagreement note. <br>3. AlphaFold HCAR2/HCAR3 monomer models reproduced via BioLib and validated vs AlphaFold DB v6. <br>4. EN one-pager + readout email incl. wet-lab benchmarking panel ask; deliverable package synced to shared drive. | [RIC-396](https://jira.novonordisk.com/browse/RIC-396) |
| | **Target safety pipeline — applications #3–#8 logged & follow-ups** | 1. CCND2 activation GREEN→RED **v1.3 offline rescore** (UHYG T2D batch, 42×2 directions): keyword-library evolution flipped one Tier 1 COSMIC oncogene call. <br>2. CTRP9/FAM3D back-filled into registry + Dashboard (pre-request-form era run made visible). <br>3. Application #8: **EJNH 3'aQTL panel, 19 targets inhibition batch** under v1.4.3 scoring; pre-check flagged 17/19 as archive-snapshot-only before running. | [RIC-391](https://jira.novonordisk.com/browse/RIC-391) |
| **Assay** | **IGWU myotube — factorial DOE + IGF/Insulin dose-response batches** | 1. **IGWU_20260730_1 Hypertrophy DOE**: treatment × arm joint-condition readout shipped in production decoupled v3.5 pipeline (**5,760 TIFFs**, 240 wells); MSTN/Bima/IGF factors reported jointly instead of collapsed arms. <br>2. **IGWU_20260811 4-plate onboard**: IGF1/IGF2/Insulin dose series (Low/Mid) × Atrophy/Hypertrophy arms; combined factorial report delivered. <br>3. On team follow-up ask, added **MYH intensity readouts (SSMD)** as report Section D + handed over raw readouts for their downstream analysis. | [RIC-394](https://jira.novonordisk.com/browse/RIC-394) |
| | **Seahorse assay imaging pipeline — three development rounds** | 1. Round 1: per-well Otsu masks produced holes from dark adipocyte clumps (nuclei signal inside holes **5.6×** surrounding) — replaced with **fixed-geometry mask templates**. <br>2. Round 2: QC observation "boundary hugs rim on some wells only" triggered per-well geometry audit — fixed-radius template systematically wrong → switched to **per-well radius templates**. <br>3. Standalone `seahorse_imaging` project spun out of RIC-375 parent work. | [RIC-375](https://jira.novonordisk.com/browse/RIC-375) |
| | **SkM Atrophy BP closeout + HepG2 ATP 4th modality** | 1. SkM Atrophy methodology BP **v2.1 summary**: core-algorithm + code-map sections added for engineering handover, metadata fields closed with assay-team input; code repository migrated to **Novo GHE**. (RIC-261, Review closeout) <br>2. HepG2 model characterization extended with **ATP safety counter-screen as 4th modality** alongside TMRM/DRUG-seq/DINOv2 (Campaigns 31/24/22, NTC-normalised); one-pager final version + supplement delivered. (RIC-381) | [RIC-261](https://jira.novonordisk.com/browse/RIC-261) / [RIC-381](https://jira.novonordisk.com/browse/RIC-381) |

---

## Tickets in period

**New**
- RIC-396 — GPR81 (HCAR1) individual target assessment

**Progressed**
- RIC-349 (v1.4 MoA layer + audit fixes), RIC-391 (applications #3–#8), RIC-395 (self-service adoption + Dashboard)
- RIC-375 (Seahorse imaging, 3 dev rounds), RIC-379 (BP poster → general-best-practice v49)
- RIC-394 (IGWU DOE + 4-plate dose response), RIC-381 (ATP 4th modality)

**In Review / closeout**
- RIC-261 (SkM Atrophy BP v2.1 + GHE migration)

**No activity this period (carried, not reported as progress)**
- RIC-390 (Lipolysis imaging), RIC-298 (Lipolysis parent), RIC-386 (DGKQ family) — no Jira comments or repo commits since July.
