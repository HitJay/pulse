---
marp: true
theme: default
paginate: true
size: 16:9
header: 'CPL 2026 Symposium · AI & Target Safety Landscape'
footer: 'Novo Nordisk R&ED · Data Science & Computational Biology'
style: |
  section { font-size: 21px; padding: 36px 56px; }
  section.title { text-align: center; justify-content: center; }
  section.title h1 { font-size: 40px; color: #003a70; margin-bottom: 10px; }
  section.title h2 { font-size: 24px; color: #00518a; border-bottom: none; font-weight: normal; }
  h1 { font-size: 30px; margin-bottom: 8px; color: #003a70; }
  h2 { font-size: 24px; color: #003a70; border-bottom: 2px solid #003a70; padding-bottom: 4px; margin-bottom: 12px; }
  h3 { font-size: 20px; color: #00518a; margin: 8px 0 4px 0; }
  table { font-size: 15px; border-collapse: collapse; margin: 8px 0; width: 100%; }
  th { background: #003a70; color: #fff; padding: 5px 8px; font-weight: 600; text-align: left; }
  td { padding: 4px 8px; border: 1px solid #d0d7de; }
  blockquote { font-size: 17px; color: #444; border-left: 4px solid #003a70; padding-left: 12px; margin: 8px 0; background: #f6f8fa; }
  code { background: #f0f3f6; padding: 2px 5px; border-radius: 3px; font-size: 16px; }
  ul, ol { margin: 4px 0; padding-left: 24px; }
  li { margin: 3px 0; line-height: 1.35; }
  .small table { font-size: 13.5px; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px 16px; }
  .card h3 { margin-top: 0; color: #003a70; }
  .bold { font-weight: 600; color: #003a70; }
---

<!-- _class: title -->

# AI Foundation Models & Target Safety
## Core Learnings from Changping Laboratory 25th HGP Symposium

**Beijing** · August 24–25, 2026  
**Core Focus**: Regulatory Foundation Models, Statistical AI Agents & Target De-risking  
**Team**: Data Science & Computational Biology

---

## 1. The Core Shift: From Sequence Reading to Causal AI

Genomics is crossing its third major threshold:

<div class="grid">
<div class="card">
<h3>Past: Observational Correlation</h3>
<ul>
<li><b>HGP (2001)</b>: Static reference genome map.</li>
<li><b>GWAS / Biobanks</b>: Statistical associations (P-values) without causal mechanism.</li>
<li><b>Safety Triage</b>: Static literature queries and bulk gene-constraint scores (pLI).</li>
</ul>
</div>
<div class="card">
<h3>Present: Predictive & Causal AI</h3>
<ul>
<li><b>Single-Cell Kinetics</b>: Absolute biophysical binding affinities on native DNA.</li>
<li><b>Genomic Foundation Models</b>: Predicting functional shifts (Δ<i>K</i><sub>d</sub>) in silico.</li>
<li><b>Safety Triage</b>: Multi-agent causal synthesis gated by statistical falsification.</li>
</ul>
</div>
</div>

> **Core Objective**: Upgrade Target Safety Landscape (TSL) from retrospective search to **mechanistic liability prediction**.

---

## 2. Regulatory Foundation Models: Decoding Non-Coding Toxicity

- **Biological Reality**: >90% of GWAS and safety-associated variants lie in non-coding regulatory DNA controlling Transcription Factor (TF) binding.
- **AI Solution (`Seq2Kd` / FOODIE Paradigm — Xiaoliang Xie & Mingchen Chen, CPL)**:
  - Measures absolute single-molecule TF-DNA affinities on native human genomes.
  - Trains deep learning foundation models (`Seq2Kd`) to predict binding affinity changes across ~500 understudied TFs.
- **Target Safety Impact**:
  - **Predicts Regulatory Collapses**: Identifies whether target perturbation strips critical TFs from vital survival genes.
  - **Mechanistic Non-Coding TSL**: Translates obscure regulatory eQTLs into quantified biophysical disruption scores (Δ<i>K</i><sub>d</sub>).

---

## 3. Statistically Gated AI Agents: Eliminating Hallucinations

- **Biological Reality**: Generic LLMs hallucinate plausible biological mechanisms, generating false-positive safety flags that derail viable drug targets.
- **AI Solution (`Fever GPT` Architecture — Xihong Lin, Harvard)**:
  - Maps 9 billion functional variant annotations across 3 billion genomic loci.
  - Couples generative LLM agents with **automated statistical falsification gates**.
- **Target Safety Impact**:
  - **Verifiable Evidence Synthesis**: Every safety claim extracted by the LLM is programmatically validated against cis-pQTL, PheWAS, and gnomAD constraint matrices.
  - **Zero-Hallucination Audit Trail**: Distinguishes true causal safety redlines from random linkage-disequilibrium noise.

---

## 4. Somatic Evolution: Separating Adaptation from Cancer

- **Biological Reality**: Detecting clonal growth in target tissue often triggers automatic carcinogenicity red flags, terminating safe programs prematurely.
- **AI & Evolutionary Solution (Peter Campbell, Quotient / ex-Sanger)**:
  - Normal aging tissue accumulates 30–40 mutations/cell/year; clonal mosaicism is ubiquitous past age 70.
  - **Key Finding**: Chronic stress-driven mutations (e.g. *FOXO1*, *GPAM* in fatty liver) preserve tissue function and are **counter-selected in cancer**.
- **Target Safety Impact**:
  - **Somatic Fitness Mapping**: Classifies whether target-driven clonal expansion represents benign physiological remodeling or malignant transformation.
  - **De-risks Chronic Targets**: Prevents premature abandonment of high-value metabolic targets.

---

## 5. Next-Gen Target Safety Pipeline: Direct Upgrades

<div class="small">

| Safety Assessment Layer | Current Standard | AI-Powered Upgrade (Post-CPL 2026) | Pipeline Decision Value |
| :--- | :--- | :--- | :--- |
| **Non-Coding Variants** | Bulk gene constraint (pLI, LOEUF) | Quantitative TF binding kinetics (`Seq2Kd`) | Pinpoints exact off-target regulatory network collapse. |
| **Safety Literature & Agent** | Uncalibrated LLM prompts / PubMed | Multi-agent pipelines with statistical gating | Eliminates false-positive toxicity flags with causal proof. |
| **Carcinogenicity & Clones** | Blanket stop-flag on clonal growth | Somatic fitness & cancer negative selection | De-risks benign adaptive tissue remodeling in metabolic programs. |
| **Cellular Phenotypes** | Isolated single-readout assays | Foundation models mapping sequence to morphology | Links HCS image phenotypes directly to underlying TF rewiring. |

</div>

---

## 6. Strategic Takeaways for Data Science

<div class="card">
<h3>Three Core Principles for Target Safety</h3>
<ul>
<li><b>1. Quantitative Kinetics > P-Values</b>: Integrate biophysical foundation models (predicting Δ<i>K</i><sub>d</sub>) to resolve non-coding target liabilities.</li>
<li><b>2. Statistical Falsification > Plausible Narratives</b>: Bound agentic LLMs with automated genetic cross-checks (cis-pQTL / PheWAS / constraint).</li>
<li><b>3. Evolutionary Grounding > Conservative Fear</b>: Distinguish benign adaptive tissue regeneration from true oncogenesis using human clonal fitness landscapes.</li>
</ul>
</div>

> **Bottom Line**: The future of target safety lies in replacing qualitative warnings with **statistically gated, biophysically grounded AI models**.
