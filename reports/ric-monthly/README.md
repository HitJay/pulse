# RIC Monthly Reports (Novo single-page table format)

Hand-curated Novo Nordisk single-page activity reports for the RIC project board.
**Independent of the Marp weekly/monthly pipeline** (`reports/monthly/`, `scripts/build_deck.py`) which renders aggregated GitHub data — this folder holds reports compiled from Jira tickets + project docs, in the Novo "Summary of activities" table template.

## Layout

```
reports/ric-monthly/
  YYYY-MM/
    monthly_report_YYYY_MM.md     # markdown draft (committed)
    monthly_report_YYYY_MM.pptx   # generated single-page deck (gitignored, rebuild anytime)
scripts/ric-monthly/
  build_ric_monthly_YYYY_MM.py    # python-pptx builder per month (committed)
```

## Build

```bash
conda run -n safety python scripts/ric-monthly/build_ric_monthly_2026_06.py
```

(Any env with `python-pptx` works; `safety` and `base` are confirmed.)

## Mirror to shared drive

```bash
cp reports/ric-monthly/2026-06/monthly_report_2026_06.pptx \
   /TDE_TV/shared_folder/QYJI/monthly_report/QYJI_2026-06-25/
```

## Conventions

- Single page, 13.333 × 7.5 inch (16:9), Novo blue header bar, 4-col table (Category / Activities / Description / Links).
- Use `Presentation()` from scratch — never load a `.pptx` as a template (XML inheritance corrupts).
- Vmerge category cells via `a:vMerge` (restart on first row, continuation on the rest).
- Skill reference: `ric-monthly-report` (see `skill_view(name='ric-monthly-report')`).
