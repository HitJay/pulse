"""
RIC Monthly Report — September 2026 (2026-08-28 -> 2026-09-25)
Two-slide executive edition (Page 1/2: Capability & Target Safety; Page 2/2: Structural Druggability & Assay).
Derived from build_ric_monthly_2026_08.py (fill_cell inline-run semantics, hyperlink auto-derivation intact).
Run: conda run -n ppt_env python scripts/ric-monthly/build_ric_monthly_2026_09.py
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
        "act": "Safety Landscape Tool — archive re-platforming & v1.4.4 gateway hardening",
        "desc": [
            ("1. Re-platformed all 281 v1.x legacy archive rows onto ", False, False),
            ("v1.4.3 live pipeline rows", True, False),
            (" across 8 chunks + c9/c10 top-ups (", False, False),
            ("297 pairs re-assessed", True, False),
            (", 0 failures); every row now carries keyword-level evidence; report links on ", False, False),
            ("862/863 rows", True, False),
            ("; ", False, False),
            ("RIC-398 closed as Done", True, False),
            (".", False, False),
            ("\n2. Engine & gateway hardening (v1.4.4): resolved Azure LiteLLM HTTP 400 gateway rejection on temperature=0.0 and disabled reasoning token overflow for Opus 5; expanded negation vocabulary (", False, False),
            ("avoiding", True, False),
            (" / ", False, False),
            ("risk is low", True, False),
            (") to eliminate false-positive REDs (PRR5).", False, False),
            ("\n3. Lifecycle governance: completed system management & IT risk documentation package for Q187219 review.", False, False),
        ],
        "link": [("RIC-349", False, False), ("RIC-398", False, False), ("RIC-404", False, False)],
    },
    {
        "cat": "", "cat_span": 0,
        "act": "Safety Landscape Tool — Dashboard Score & Keywords columns, search expansion",
        "desc": [
            ("1. Dashboard table enhanced with dedicated ", False, False),
            ("Score", True, False),
            (" (numerical sortable) and ", False, False),
            ("Matched Keywords", True, False),
            (" columns displaying quantitative weights and toxicological risk tags.", False, False),
            ("\n2. Global search filter expanded to support ", False, False),
            ("toxicity keywords", True, False),
            (" (e.g. pancreatitis, seizure, lactic acidosis), exact scores, and colleague requester initials (", False, False),
            ("zhco, ylv, ejnh", True, False),
            ("); updated search placeholder.", False, False),
            ("\n3. Enforced ", False, False),
            ("direction-matched NCBN gold labels", True, False),
            (" to eliminate cross-direction attribution overrides (ACOX1, ACACA, MEN1, NLRP3).", False, False),
        ],
        "link": [("RIC-395", False, False)],
    },
    {
        "cat": "", "cat_span": 0,
        "act": "Druggability Agent — v0.2.0 platform architecture & peptide engineering framework",
        "desc": [
            ("1. Codebase elevated to top-level ", False, False),
            ("druggability namespace (v0.2.0)", True, False),
            (", retaining bbbkit backward-compatibility shim; all ", False, False),
            ("156 unit tests passing", True, False),
            ("; codified persistent Agent skill peptide-druggability-assessment.", False, False),
            ("\n2. Deployed multi-tier peptide toolset: Layer 1 ", False, False),
            ("PRODIGY contact affinity", True, False),
            (" (ΔG/Kd); Layer 2 in silico Alanine scanning & 20-AA matrix; Layer 3 GPU short-MD ensemble MM/GBSA (", False, False),
            (">2,100 ns/day on A100", True, False),
            (") resolving static void artifacts; Layer 4 subtype selectivity audit.", False, False),
            ("\n3. Standardized ", False, False),
            ("DrugCLIP contrastive AI screening", True, False),
            (" (NeurIPS 2023) on A100 for automated pocket extraction and sub-second chemical library retrieval.", False, False),
        ],
        "link": [("RIC-403", False, False)],
    },
    {
        "cat": "Targets", "cat_span": 2,
        "act": "Target safety pipeline — periodic round W38, individual requests & PEX16 fix",
        "desc": [
            ("1. Application #12 (W38 periodic round for YLV): 47 unique pairs evaluated: ", False, False),
            ("18 RED | 13 YELLOW | 16 GREEN", True, False),
            ("; ANXA5 dual-direction evaluated (Act YELLOW 72 / Inh GREEN 0); 100% programmatic coverage audit.", False, False),
            ("\n2. Application #9 & #11: GPR68 inhibition (", False, False),
            ("GREEN 0", True, False),
            (", CCEG) and PIKFYVE inhibition (", False, False),
            ("RED 126", True, False),
            (", ZHCO; human clinical exposure follow-up on apilimod).", False, False),
            ("\n3. Resolved PEX16 negation mis-suppression (", False, False),
            ("RIC-400", True, False),
            ("): HGNC alias expansion in PubMed query; MUL1 re-run and post-delivery evidence addendum on murine HCC liability (PMID 37962001).", False, False),
        ],
        "link": [("RIC-391", False, False), ("RIC-400", False, False)],
    },
    {
        "cat": "", "cat_span": 0,
        "act": "siGRB10 off-target safety evaluation — PRR5, LTN1, ALKBH8, LRRCC1 (liver focus)",
        "desc": [
            ("1. Liver-focused in vivo tolerability evaluation of 4 off-target candidates under inhibition direction: ", False, False),
            ("3 YELLOW", True, False),
            (" (PRR5, LTN1, ALKBH8) | ", False, False),
            ("1 GREEN", True, False),
            (" (LRRCC1); completed in ", False, False),
            ("~4.5 min end-to-end", True, False),
            (" (~1.1 min/target).", False, False),
            ("\n2. PRR5 root-cause diagnosis: resolved false-positive RED via negative-context negation fix (", False, False),
            ("Score 44 YELLOW", True, False),
            ("; selective KO avoids Rictor/mTOR lethality; gnomAD pLI ≈ 0).", False, False),
            ("\n3. Delivered 7-slide executive Marp deck (.pptx + .html) with clinical/genetic liabilities and monitoring recommendations to requester YLV.", False, False),
        ],
        "link": [("RIC-405", False, False)],
    },
]

# ── Slide 2 Data: Structural Druggability & Assay ──
SLIDE_2_ROWS = [
    {
        "cat": "Targets", "cat_span": 3,
        "act": "GPR81 (HCAR1) target assessment — orthosteric vs allosteric modes & OpenFEP",
        "desc": [
            ("1. Receptor structural alignment (human 8Z8A vs cryo-EM HCAR2 8J6P): lactate/niacin orthosteric centers superimpose within 0.75 Å; maps allosteric agonist to TM5-TM6-ECL2 crevice (", False, False),
            ("17.7 Å separation", True, False),
            ("); corroborated by ebBRET literature establishing Agonist 1 as ", False, False),
            ("ago-PAM", True, False),
            (" vs AZ1/AZ7136 as ", False, False),
            ("orthosteric agonists", True, False),
            (".", False, False),
            ("\n2. Completed converged ", False, False),
            ("congeneric OpenFEP simulation", True, False),
            (" across all 3 legs (constrained pyridones lead c28/c26/c30/c38 vs AZ series).", False, False),
            ("\n3. Delivered ", False, False),
            ("14-slide executive presentation deck", True, False),
            (" (pptx/pdf), interactive 3D WebGL report, and paste-ready readout email to colleague Huan (UHYG).", False, False),
        ],
        "link": [("RIC-396", False, False)],
    },
    {
        "cat": "", "cat_span": 0,
        "act": "GIGYF1–GRB10/14–INSR axis — clinical genetics perturbation & molecular glue audit",
        "desc": [
            ("1. In silico clinical genetics perturbation on 1.79 Å GIGYF1:GRB10 complex: identified ", False, False),
            ("p.Tyr498Cys with massive ΔΔG = +2.74 kcal/mol", True, False),
            (" (>80-fold affinity loss), directly validating GIGYF1-GRB10 disruption as causal driver of T2D predisposition in humans (", False, False),
            ("OR = 5.91", True, False),
            ("); p.Trp494Arg (+1.80 kcal/mol) and p.Ser474Ter (+5.88 kcal/mol).", False, False),
            ("\n2. A100 GPU explicit-solvent MD (1,103 solute atoms in TIP3P): backbone RMSD converged at ", False, False),
            ("0.36 ± 0.08 Å", True, False),
            ("; identified Pro1 (-50.4 kcal/mol) and Leu4 (-40.0 kcal/mol) as core anchors.", False, False),
            ("\n3. Delivered ", False, False),
            ("8-slide executive Marp deck", True, False),
            (" (pptx/pdf) with Tier 0 in silico virtual screening recommendations for JXDL.", False, False),
        ],
        "link": [("RIC-407", False, False)],
    },
    {
        "cat": "", "cat_span": 0,
        "act": "OXTR individual target assessment — structural pharmacology & subtype selectivity",
        "desc": [
            ("1. Structural pharmacology & selectivity audit across human active (7QVM/7RYC) vs inactive (6TPK) OXTR, and subtype counter-screen with vasopressin V2R (7DW9).", False, False),
            ("\n2. Pro7Gly selectivity mechanism: V2R 3.51 Å Helix I constriction + ECL3 Leu302 hydrophobic mismatch causes severe steric clash on V2R while OXTR accommodates Gly7.", False, False),
            ("\n3. Confirmed Leu8 as solvent-exposed exit vector for fatty-acid acylation (Lys8 substitution favorable at ", False, False),
            ("-12.16 kcal/mol", True, False),
            (" with unobstructed 3D conical clearance, rationalizing Lilly long-acting design); delivered standalone 3Dmol.js HTML dossiers.", False, False),
        ],
        "link": [("RIC-403", False, False)],
    },
    {
        "cat": "Assay", "cat_span": 2,
        "act": "IGWU myotube — MEK inhibitor factorial & IGF/Insulin dose-response repeat",
        "desc": [
            ("1. IGWU_20260907_1 (MEK Inhibitor Factorial): U0126/PD98059 × dose (0.16–20 µM) × IGF ligand plate onboarded on decoupled v3.5 pipeline (", False, False),
            ("240/240 wells", True, False),
            ("); identified phenotypic split at 20 µM: negative nuclei count alongside peaked morphological hypertrophy (length ", False, False),
            ("+1.52 SSMD", True, False),
            (", fusion index ", False, False),
            ("+1.75 SSMD", True, False),
            (").", False, False),
            ("\n2. IGWU_20260907_2 (IGF/Insulin Dose-Response Repeat): 240 wells processed; confirmed consistent negative length dose-response across all three ligands (-5% to -14%, strongest IGF2 ", False, False),
            ("-1.52 SSMD", True, False),
            (" at 4 nM) with counter-directional MYH intensity elevation (IGF2_1000 ", False, False),
            ("+3.06 SSMD", True, False),
            (") reflecting differentiation remodeling.", False, False),
        ],
        "link": [("RIC-394", False, False)],
    },
    {
        "cat": "", "cat_span": 0,
        "act": "Seahorse assay imaging pipeline — Production Baseline Gen 2.2 release",
        "desc": [
            ("1. Released ", False, False),
            ("Production Baseline Gen 2.2", True, False),
            (" (Multi-scale LoG + Per-Well Kasa Circle Refitting + Soft-Edge Profile + Rigid Pillar Dynamics) across 5x Seahorse automated counting.", False, False),
            ("\n2. Engineering enhancements: Per-well Kasa circle refit resolves translation offsets (systematic ", False, False),
            ("dx = -66.5 px", True, False),
            (" rigid shift on SkM) preventing rim eccentricity and tissue clipping; synchronized consensus pillar coordinates; radial profile soft-edge expansion (r = 795 px Adipo, 805 px SkM, 815–845 px HepG2).", False, False),
            ("\n3. Slide 4 microscopic gallery overhaul: expanded 4-column microscopic image strip (", False, False),
            ("+16.2% width", True, False),
            (") with absolute coordinate grid stabilization for publication-grade PPTX/PDF rendering.", False, False),
        ],
        "link": [("RIC-375", False, False)],
    },
]

PAGES = [
    ("Page 1/2", SLIDE_1_ROWS, [(1, 3), (4, 2)]),
    ("Page 2/2", SLIDE_2_ROWS, [(1, 3), (4, 2)]),
]

OUT = "reports/ric-monthly/2026-09/monthly_report_2026_09.pptx"

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
    add_run(p, f"     │     QYJI     │     {page_str}     │     2026/09/25     │     ", bold=False, size_pt=9, color=NN_BLUE_LITE)
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
