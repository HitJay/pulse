"""
RIC Monthly Report — October 2026 (2026-09-25 -> 2026-10-30)
Two-slide executive edition (Page 1/2: Capability & Target Safety; Page 2/2: Structural Druggability & Assay).
Derived from build_ric_monthly_2026_09.py (fill_cell inline-run semantics, hyperlink auto-derivation intact).
Run: conda run -n ppt_env python scripts/ric-monthly/build_ric_monthly_2026_10.py
(from /das/user/QYJI/pulse repo root)
"""

import re

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from lxml import etree

JIRA_BASE = "https://jira.novonordisk.com/browse/"
RIC_RE = re.compile(r"RIC-\d+")

# ── Colours ──
NN_BLUE      = RGBColor(0x00, 0x38, 0x65)
NN_BLUE_LITE = RGBColor(0xCC, 0xD9, 0xE8)
WHITE        = RGBColor(0xFF, 0xFF, 0xFF)
DARK_GREY    = RGBColor(0x26, 0x26, 0x26)
GREY_BG      = RGBColor(0xF2, 0xF2, 0xF2)

# ── Font sizes (user-confirmed 2026-05-28, do not shrink) ──
SZ_HEADER    = 11
SZ_BODY      = 9.5
SZ_LINK      = 8.5
SZ_TITLE_BAR = 14
LINE_SPACING = 12

def set_cell_bg(cell, rgb):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    for tag in ['a:solidFill', 'a:gradFill', 'a:noFill']:
        for el in tcPr.findall(qn(tag)):
            tcPr.remove(el)
    solidFill = etree.SubElement(tcPr, qn('a:solidFill'))
    srgb = etree.SubElement(solidFill, qn('a:srgbClr'))
    srgb.set('val', f'{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}')

def add_run(para, text, bold=False, size_pt=SZ_BODY, color=DARK_GREY, italic=False, hyperlink=None):
    run = para.add_run()
    run.text = text
    run.font.bold = bold
    run.font.italic = italic
    run.font.size = Pt(size_pt)
    run.font.color.rgb = color
    run.font.name = 'Calibri'
    if hyperlink:
        run.hyperlink.address = hyperlink
    return run

def _style_para(para):
    para.space_before = Pt(0.5)
    para.space_after  = Pt(0.5)
    para.line_spacing = Pt(LINE_SPACING)

def fill_cell(cell, lines, header=False, category=False, link=False):
    tf = cell.text_frame
    tf.word_wrap = True
    tf.margin_left   = Inches(0.06)
    tf.margin_right  = Inches(0.06)
    tf.margin_top    = Inches(0.04)
    tf.margin_bottom = Inches(0.04)
    c = WHITE if header else (NN_BLUE if category else DARK_GREY)
    sz = SZ_HEADER if header else (SZ_BODY if not link else SZ_LINK)

    para = tf.paragraphs[0]
    _style_para(para)
    para_used = False

    for (text, bold, italic) in lines:
        if link:
            if para_used:
                para = tf.add_paragraph(); _style_para(para)
            m = RIC_RE.search(text)
            href = JIRA_BASE + m.group(0) if m else None
            link_color = RGBColor(0x00, 0x56, 0x9E) if href else c
            add_run(para, text, bold=bold, italic=italic, size_pt=sz, color=link_color, hyperlink=href)
            para_used = True
            continue

        segments = text.split('\n')
        for si, seg in enumerate(segments):
            if si > 0:
                para = tf.add_paragraph(); _style_para(para)
                para_used = False
            if seg == '' and not para_used:
                continue
            add_run(para, seg, bold=bold, italic=italic, size_pt=sz, color=c)
            para_used = True

def vmerge_restart(cell):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    for el in tcPr.findall(qn('a:vMerge')):
        tcPr.remove(el)
    vm = etree.SubElement(tcPr, qn('a:vMerge'))
    vm.set('val', 'restart')

def vmerge_cont(cell):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    for el in tcPr.findall(qn('a:vMerge')):
        tcPr.remove(el)
    etree.SubElement(tcPr, qn('a:vMerge'))

# ── Slide 1 Data: Capability & Target Safety ──
SLIDE_1_ROWS = [
    {
        "cat": "Capability", "cat_span": 3,
        "act": "Safety Landscape Tool — v1.4.7–v1.4.9 local Qwen baseline, Color_Basis & marketplace benchmark",
        "desc": [
            ("1. Re-baselined scoring pipeline to local ", False, False),
            ("qwen3.8-27b-fp8", True, False),
            (" (TP2, 16k ctx) with backend-conditional RED dual gate (", False, False),
            ("max_kw ≥ 80", True, False),
            (") & Laya sanity gate at ", False, False),
            ("T = 0.7", True, False),
            (" (", False, False),
            ("0.6492 live gate acc", True, False),
            (" on NCBN-305); tested and closed 4 optimization paths with archived A/B evidence (", False, False),
            ("v1.4.9", True, False),
            (").", False, False),
            ("\n2. Benchmarked 3 marketplace summary backends on frozen 300-target snapshot: established ", False, False),
            ("gemini_4_argon (0.6426 acc", True, False),
            (", 76 min) and ", False, False),
            ("kimi_k3 (0.6426 acc)", True, False),
            (" as fallback #1/#2.", False, False),
            ("\n3. Added ", False, False),
            ("Color_Basis & Color_Chain", True, False),
            (" provenance tracking (", False, False),
            ("900/900", True, False),
            (" benchmark replay equivalence), target-level checkpoint.jsonl resume, and ", False, False),
            ("STAT3 inhibition YELLOW", True, False),
            (" gold-conflict adjudication.", False, False),
        ],
        "link": [("RIC-349", False, False)],
    },
    {
        "cat": "", "cat_span": 0,
        "act": "Safety gate dry/wet consistency study — 175 HepG2 targets vs ATP & TMRM toxicity",
        "desc": [
            ("1. Evaluated ", False, False),
            ("175/175 RIC-381 HepG2 siRNA targets", True, False),
            (" under inhibition direction (", False, False),
            ("92 RED | 64 YELLOW | 19 GREEN", True, False),
            (") on checkpointed local vLLM backend and aligned ", False, False),
            ("172 targets", True, False),
            (" against wet-lab ATP, TMRM ΔΨm, and imaging toxicity readouts.", False, False),
            ("\n2. Quantified near-zero correlation across all wet endpoints (", False, False),
            ("Spearman r = -0.06 to +0.15", True, False),
            ("; strata toxic rate RED 27% / YELLOW 33% / GREEN 24%), establishing expected ", False, False),
            ("construct independence", True, False),
            (" (human clinical/genetic safety vs acute cellular viability).", False, False),
            ("\n3. Confirmed safety gate remains authoritative for ", False, False),
            ("Red line item 5", True, False),
            (", with 25 Non-RED & wet-toxic cases routed for P1 calibration (", False, False),
            ("RIC-409 closed as Done", True, False),
            (").", False, False),
        ],
        "link": [("RIC-409", False, False), ("RIC-381", False, False)],
    },
    {
        "cat": "", "cat_span": 0,
        "act": "Proteome-wide PPI screening (RF2-PPI Science 2025) & disease-variant interface mapping",
        "desc": [
            ("1. Reproduced ", False, False),
            ("RF2-PPI", True, False),
            (" (Zhang et al., Science 2025) across all ", False, False),
            ("33,000 benchmark pairs", True, False),
            (" on 6× A100 GPUs: weighted ", False, False),
            ("AUCPR = 0.262 (262×", True, False),
            (" vs 1:1000 random baseline), ", False, False),
            ("20.8% recall at 90% precision", True, False),
            (" (623 pairs, 0 top-rank FP), and ", False, False),
            ("43.2% recall", True, False),
            (" on large interfaces; author score parity ", False, False),
            ("Pearson r = 0.919", True, False),
            (" across 8,977 pairs.", False, False),
            ("\n2. Built ", False, False),
            ("interface-variants module", True, False),
            (" (Pei et al. 2026 method; ", False, False),
            ("22 unit tests passing", True, False),
            (") mapping dual-evidence pathogenic SAVs (AlphaMissense + UniProt) onto 3D PPI interfaces (6 Å cutoff).", False, False),
            ("\n3. Delivered ", False, False),
            ("1-page biology-facing proposal slide", True, False),
            (" (PPTX + @3x PNG + speaker notes) linking proteome triage to ", False, False),
            ("RIC-407", True, False),
            (" GIGYF1–GRB10 glue campaign.", False, False),
        ],
        "link": [("RIC-410", False, False), ("RIC-407", False, False)],
    },
    {
        "cat": "Targets", "cat_span": 2,
        "act": "Target safety pipeline — periodic rounds W40–W44 & ZHCO T2D/obesity panel (298 pairs)",
        "desc": [
            ("1. Processed weekly Highway/periodic rounds for YLV with 100% coverage & Color_Basis audit: ", False, False),
            ("W40", True, False),
            (" (61 pairs: 24R/31Y/6G), ", False, False),
            ("W41", True, False),
            (" (63 pairs: 16R/33Y/14G), ", False, False),
            ("W42", True, False),
            (" (60 pairs: 14R/31Y/15G), ", False, False),
            ("W43", True, False),
            (" (62 pairs: 10R/43Y/9G), and ", False, False),
            ("W44", True, False),
            (" (63 pairs: 15R/35Y/13G).", False, False),
            ("\n2. Delivered ", False, False),
            ("ZHCO T2D/obesity 25-gene bidirectional panel", True, False),
            (" (", False, False),
            ("50 pairs", True, False),
            (": 45 fresh + 5 legacy; ", False, False),
            ("13 RED | 20 YELLOW | 17 GREEN", True, False),
            (").", False, False),
            ("\n3. Enforced backend-aware RED dual gate in delivery verification (check_color_basis.py, ", False, False),
            ("0 errors across W41–W44", True, False),
            (") and refreshed PTH2R activation live row.", False, False),
        ],
        "link": [("RIC-391", False, False)],
    },
    {
        "cat": "", "cat_span": 0,
        "act": "Ad-hoc target safety evaluations — FAP conjugate anchor, PROKR1, AGTR1 & APOA5",
        "desc": [
            ("1. ", False, False),
            ("FAP", True, False),
            (" (App #14, YZGC MASH/CKD/HF siRNA-conjugate anchor): ", False, False),
            ("GREEN (0)", True, False),
            (" both directions; decoupled historical cell-ablation cachexia/anemia (PMID 23712428) from benign enzymatic/expression loss (Fap KO viable, gnomAD ", False, False),
            ("pLI ≈ 0", True, False),
            ("); defined ", False, False),
            ("Fc effector-silence (LALA-PG)", True, False),
            (" & sFAP sink boundaries.", False, False),
            ("\n2. ", False, False),
            ("PROKR1 & AGTR1", True, False),
            (" (Apps #16–#17, EJNH T2D/obesity): PROKR1-inh ", False, False),
            ("GREEN (0)", True, False),
            ("; PROKR1-act reclassified ", False, False),
            ("RED → YELLOW (84)", True, False),
            (" after PubMed audit disproved hypotension claim; AGTR1-act ", False, False),
            ("YELLOW (100)", True, False),
            (" (LLM downgrade; pressor/renal remodeling liabilities).", False, False),
            ("\n3. ", False, False),
            ("APOA5", True, False),
            (" (App #20, EJNH T2D): fresh dual-direction run on local vLLM (~1 min/dir): activation ", False, False),
            ("GREEN (0)", True, False),
            (", inhibition ", False, False),
            ("YELLOW (75)", True, False),
            (".", False, False),
        ],
        "link": [("RIC-391", False, False)],
    },
]

# ── Slide 2 Data: Structural Druggability & Assay ──
SLIDE_2_ROWS = [
    {
        "cat": "Targets", "cat_span": 1,
        "act": "TSPO ligands (PK11195, emapunil, etifoxine, FGIN-1-27, alpidem) — target deconvolution & FEP",
        "desc": [
            ("1. Multi-layer off-target deconvolution across 5 ligands (ChEMBL/PubChem + GTEx + OpenTargets + 17-pocket Vina gate + SwissTargetPrediction + ", False, False),
            ("Boltz-2 de novo co-folding", True, False),
            ("): proved ", False, False),
            ("CAR (NR1I3) is the dominant metabolic target of PK11195", True, False),
            (" (IC50 ", False, False),
            ("25–56 nM", True, False),
            (", confirmed by ", False, False),
            ("5 independent method families", True, False),
            (", Boltz-2 CAR-LBD centroid 2.52 Å from crystal agonist).", False, False),
            ("\n2. Exposure-occupancy gate: ", False, False),
            ("emapunil", True, False),
            (" selectively engages TSPO (", False, False),
            ("13.5% occ", True, False),
            (" at 90 mg qd, Ki 6.4 nM); ", False, False),
            ("etifoxine (<0.01% occ", True, False),
            (", Ki 7.8 µM) & ", False, False),
            ("alpidem", True, False),
            (" fail TSPO occupancy at clinical exposure (alpidem acts via GABA-A BZD site).", False, False),
            ("\n3. Completed ", False, False),
            ("250 ps restrained MD + annihilation alanine-scanning TI (21 anchors)", True, False),
            (" across known & fpocket novel pockets (identifying TSPO dimer pocket 4RYI_p26 LEU58 & GABA-A 6X3X_p78 SER196); delivered HTML reports, 1920×1080 one-pager, and ", False, False),
            ("7-slide EN/CN decks", True, False),
            (" to ZHCO/ZC.", False, False),
        ],
        "link": [("RIC-408", False, False)],
    },
    {
        "cat": "Assay", "cat_span": 2,
        "act": "IGWU myotube atrophy — zero-shot foundation model benchmark & ACVR / GRB10 batch readouts",
        "desc": [
            ("1. ", False, False),
            ("Zero-shot foundation model benchmark", True, False),
            (" across ", False, False),
            ("720 wells", True, False),
            (" (3 IGWU batches): evaluated Google ", False, False),
            ("EmbeddingGemma-2", True, False),
            (" (740M), Meta ", False, False),
            ("SAM 2.1", True, False),
            (", and ", False, False),
            ("SAM 3", True, False),
            (" (848M) vs v3.5 decoupled CellProfiler. Embedding variance is dominated by batch (", False, False),
            ("η² = 0.12–0.36", True, False),
            (" vs condition ~0.04; within-batch kNN lift collapses to ", False, False),
            ("1.1×", True, False),
            ("); SAM 2.1/3 over-segment inter-fibre background (", False, False),
            ("IoU = 0.412 / 0.408", True, False),
            (") — all 3 rejected zero-shot, confirming ", False, False),
            ("CellProfiler combination_mask", True, False),
            (" as authoritative.", False, False),
            ("\n2. Onboarded ", False, False),
            ("IGWU_20260923_1", True, False),
            (" (ACVR factorial, ", False, False),
            ("240/240 wells", True, False),
            (": ALK4/ALK5 inhibitors increase length ", False, False),
            ("+17.0% to +17.9%, +1.27 SSMD", True, False),
            (") and ", False, False),
            ("IGWU_20260923_2", True, False),
            (" (GRB10 siRNA, ", False, False),
            ("240/240 wells", True, False),
            (": GRB10 neutral, IGFBP5 KD -11.5% length); fixed CIFS concurrent hardlink lock via copyfile.", False, False),
        ],
        "link": [("RIC-261", False, False), ("RIC-394", False, False)],
    },
    {
        "cat": "", "cat_span": 0,
        "act": "Seahorse assay imaging pipeline — PR #2 multi-lineage 900-well benchmark & BP portal release",
        "desc": [
            ("1. Executed full generalization benchmark of ", False, False),
            ("PR #2", True, False),
            (" (per-well rim & pillar detection engine, co-developed with AXVN) across the ", False, False),
            ("15-batch production panel (900 wells, 7,200 fields)", True, False),
            (" spanning Mature Adipocytes, Skeletal Muscle, and HepG2.", False, False),
            ("\n2. Confirmed ", False, False),
            ("1.0–2.0 px median pillar residual", True, False),
            (" (eliminating legacy 6–7 px rigid offset) with zero parameter retuning; unmasked ", False, False),
            ("+4.45% cell count", True, False),
            (" on 3D adipocytes (recovering a hidden knockdown respiration gain) and verified safe fallback on a 35–60 px stage-shifted plate (", False, False),
            ("-0.63% delta", True, False),
            (").", False, False),
            ("\n3. Updated ", False, False),
            ("Gen 2.2 Best Practice summary", True, False),
            (" (§11.5) with automated confidentiality/vendor leakage assertions for standalone portal publishing.", False, False),
        ],
        "link": [("RIC-375", False, False)],
    },
    {
        "cat": "Capability", "cat_span": 1,
        "act": "RIC portfolio review (2026 Goals / Highway alignment) & legacy ticket hygiene closeout",
        "desc": [
            ("1. Completed ", False, False),
            ("RIC Portfolio Review v2.4", True, False),
            (" aligning active tickets and FTE allocation against ", False, False),
            ("2026 Goals (G1–G8)", True, False),
            (" and the ", False, False),
            ("NNRCC Highway / Red line operational model", True, False),
            (" (6 MOA clusters, stop/go de-risking narrative).", False, False),
            ("\n2. Executed structured ", False, False),
            ("Closure sub-variant workflow", True, False),
            (" (Description posterity rewrite + timeline/outcome table + Done gate fields + assignee verification) across ", False, False),
            ("14 completed or superseded legacy tickets", True, False),
            (" (", False, False),
            ("RIC-247", True, False),
            (" decoupled pipeline umbrella, ", False, False),
            ("RIC-298", True, False),
            (" adipocyte lipolysis vAssay, ", False, False),
            ("RIC-358", True, False),
            (" EE TMRM support, plus 11 completed assay/campaign cards).", False, False),
        ],
        "link": [("RIC-247", False, False), ("RIC-298", False, False), ("RIC-358", False, False)],
    },
]

PAGES = [
    ("Page 1/2", SLIDE_1_ROWS, [(1, 3), (4, 2)]),
    ("Page 2/2", SLIDE_2_ROWS, [(2, 2)]),
]

OUT = "reports/ric-monthly/2026-10/monthly_report_2026_10.pptx"

# ── Build ──
prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

ML = Inches(0.25); MR = Inches(0.25); MT = Inches(0.15)
W = prs.slide_width; H = prs.slide_height
HDR_H = Inches(0.42)

for page_str, page_rows, vmerge_spans in PAGES:
    slide = prs.slides.add_slide(blank_layout)

    # Header bar
    hdr = slide.shapes.add_shape(1, ML, MT, W - ML - MR, HDR_H)
    hdr.fill.solid(); hdr.fill.fore_color.rgb = NN_BLUE; hdr.line.fill.background()
    tf = hdr.text_frame; tf.word_wrap = False
    tf.margin_left = Inches(0.08); tf.margin_top = Inches(0.04)
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.LEFT
    add_run(p, "Summary of activities", bold=True, size_pt=SZ_TITLE_BAR, color=WHITE)
    add_run(p, f"     │     QYJI     │     {page_str}     │     2026/10/30     │     ", bold=False, size_pt=9, color=NN_BLUE_LITE)
    add_run(p, "Novo Nordisk®", bold=True, size_pt=10, color=WHITE)

    # Table layout
    TBL_T = MT + HDR_H + Inches(0.06)
    TBL_H = H - TBL_T - Inches(0.1)
    TBL_W = W - ML - MR
    N_ROWS = 1 + len(page_rows); N_COLS = 4

    tbl_shape = slide.shapes.add_table(N_ROWS, N_COLS, ML, TBL_T, TBL_W, TBL_H)
    tbl = tbl_shape.table

    col_w = [int(TBL_W * 0.08), int(TBL_W * 0.16), int(TBL_W * 0.61), int(TBL_W * 0.15)]
    col_w[-1] = TBL_W - sum(col_w[:-1])
    for ci, w in enumerate(col_w):
        tbl.columns[ci].width = w

    HDR_ROW_H  = Inches(0.30)
    DATA_ROW_H = int((TBL_H - HDR_ROW_H) / max(len(page_rows), 1))
    tbl.rows[0].height = HDR_ROW_H
    for ri in range(1, N_ROWS):
        tbl.rows[ri].height = DATA_ROW_H

    for ci, hh in enumerate(["Category", "List of activities", "Brief description", "Relevant links/files"]):
        cell = tbl.cell(0, ci)
        set_cell_bg(cell, NN_BLUE)
        fill_cell(cell, [(hh, True, False)], header=True)

    for ri, row in enumerate(page_rows):
        dr = ri + 1
        bg = GREY_BG if dr % 2 == 0 else WHITE
        cat_cell = tbl.cell(dr, 0)
        set_cell_bg(cat_cell, NN_BLUE_LITE)
        fill_cell(cat_cell, [(row["cat"], True, False)] if row["cat"] else [("", False, False)], category=bool(row["cat"]))
        act_cell = tbl.cell(dr, 1)
        set_cell_bg(act_cell, bg); fill_cell(act_cell, [(row["act"], True, False)])
        desc_cell = tbl.cell(dr, 2)
        set_cell_bg(desc_cell, bg); fill_cell(desc_cell, row["desc"])
        link_cell = tbl.cell(dr, 3)
        set_cell_bg(link_cell, bg); fill_cell(link_cell, row["link"], link=True)

    for (start, span) in vmerge_spans:
        vmerge_restart(tbl.cell(start, 0))
        for i in range(1, span):
            vmerge_cont(tbl.cell(start + i, 0))

prs.save(OUT)
print("Saved:", OUT)
