from __future__ import annotations

import json
from pathlib import Path

from modality_lite.models import AssessmentResult


def write_json(result: AssessmentResult, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result.as_dict(), ensure_ascii=False, indent=2), encoding="utf-8")


def render_markdown(result: AssessmentResult) -> str:
    case = result.case
    features = result.target_features
    lines = [
        f"# Modality fit assessment: {features.symbol}",
        "",
        "## Input",
        "",
        f"- Target: `{case.target}`",
        f"- Intended direction: `{case.intended_direction or 'not provided'}`",
        f"- Tissue context: `{case.tissue_context or 'not provided'}`",
        "",
        "## Target features",
        "",
        f"- Approved symbol: `{features.symbol}`",
        f"- Approved name: {features.approved_name or 'unknown'}",
        f"- Ensembl ID: `{features.ensembl_id or 'unknown'}`",
        f"- Biotype: `{features.biotype or 'unknown'}`",
        f"- Source: {features.source_url or 'not available'}",
        "",
        "## Modality fit table",
        "",
        "| Modality | Fit | Reason | Missing evidence |",
        "|---|---|---|---|",
    ]
    for fit in result.modality_fits:
        reason = "<br>".join(fit.reason) if fit.reason else ""
        missing = "<br>".join(fit.missing_evidence) if fit.missing_evidence else ""
        lines.append(f"| `{fit.modality}` | **{fit.fit}** | {reason} | {missing} |")

    lines.extend(["", "## Evidence fields", ""])
    for fit in result.modality_fits:
        lines.append(f"### {fit.modality}")
        if fit.evidence_fields:
            for item in fit.evidence_fields:
                lines.append(f"- {item}")
        else:
            lines.append("- No direct evidence field triggered in MVP rules.")
        lines.append("")
    return "\n".join(lines)


def write_markdown(result: AssessmentResult, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_markdown(result), encoding="utf-8")