from __future__ import annotations

import argparse
import csv
from pathlib import Path

from modality_lite.models import AssessmentCase, AssessmentResult
from modality_lite.report import write_json, write_markdown
from modality_lite.scoring import assess_modalities
from modality_lite.sources.opentargets import OpenTargetsError, fetch_target_features


def assess_case(case: AssessmentCase) -> AssessmentResult:
    features = fetch_target_features(case.target)
    modality_fits = assess_modalities(case, features)
    return AssessmentResult(case=case, target_features=features, modality_fits=modality_fits)


def command_assess(args: argparse.Namespace) -> int:
    case = AssessmentCase(target=args.target, intended_direction=args.direction, tissue_context=args.tissue)
    try:
        result = assess_case(case)
    except OpenTargetsError as exc:
        print(f"OpenTargets error: {exc}")
        return 2

    out_dir = Path(args.out) if args.out else Path("output") / "modality_lite" / result.target_features.symbol
    write_json(result, out_dir / "assessment.json")
    write_markdown(result, out_dir / "assessment.md")
    print(f"Wrote {out_dir / 'assessment.json'}")
    print(f"Wrote {out_dir / 'assessment.md'}")
    return 0


def command_batch(args: argparse.Namespace) -> int:
    input_path = Path(args.input)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    with input_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            target = row.get("target") or row.get("symbol")
            if not target:
                failures.append("row without target/symbol")
                continue
            case = AssessmentCase(
                target=target,
                intended_direction=row.get("direction") or row.get("intended_direction") or None,
                tissue_context=row.get("tissue") or row.get("tissue_context") or None,
            )
            try:
                result = assess_case(case)
            except OpenTargetsError as exc:
                failures.append(f"{target}: {exc}")
                continue
            target_dir = out_dir / result.target_features.symbol
            write_json(result, target_dir / "assessment.json")
            write_markdown(result, target_dir / "assessment.md")

    if failures:
        print("Completed with failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"Wrote batch results to {out_dir}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Lightweight target-to-modality fit assessment.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    assess = subparsers.add_parser("assess", help="Assess a single target.")
    assess.add_argument("target")
    assess.add_argument("--direction", help="Optional intended direction, e.g. inhibit, knockdown, agonize, degrade.")
    assess.add_argument("--tissue", help="Optional tissue context, e.g. liver, adipose, skeletal_muscle.")
    assess.add_argument("--out", help="Output directory.")
    assess.set_defaults(func=command_assess)

    batch = subparsers.add_parser("batch", help="Assess targets from a CSV with target,direction,tissue columns.")
    batch.add_argument("input")
    batch.add_argument("--out", required=True, help="Output directory.")
    batch.set_defaults(func=command_batch)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())