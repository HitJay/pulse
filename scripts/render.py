#!/usr/bin/env python3
"""
render.py – 使用 Jinja2 模板渲染周报/月报 Markdown。

用法:
    python scripts/render.py weekly                    # 生成本周周报
    python scripts/render.py weekly --week 2026-W19    # 指定周
    python scripts/render.py monthly                   # 生成本月月报
    python scripts/render.py monthly --month 2026-05   # 指定月
"""

from __future__ import annotations

import json
import shutil
import sys
from datetime import datetime, timedelta
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# ── 路径 ────────────────────────────────────────────────────────

PULSE_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = PULSE_ROOT / "templates"
REPORTS_DIR = PULSE_ROOT / "reports"
DOCS_REPORTS_DIR = PULSE_ROOT / "docs" / "reports"
CACHE_DIR = PULSE_ROOT / ".cache"

# ── Jinja2 环境 ──────────────────────────────────────────────────

env = Environment(
    loader=FileSystemLoader(str(TEMPLATES_DIR)),
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True,
)


# ── 工具函数 ─────────────────────────────────────────────────────


def get_iso_week() -> str:
    """返回当前 ISO 周，如 '2026-W19'。"""
    now = datetime.now()
    return f"{now.isocalendar()[0]}-W{now.isocalendar()[1]:02d}"


def get_week_date_range(week_str: str) -> str:
    """将 '2026-W19' 转换为日期范围字符串。"""
    year, week = week_str.split("-W")
    monday = datetime.fromisocalendar(int(year), int(week), 1)
    sunday = datetime.fromisocalendar(int(year), int(week), 7)
    return f"{monday.strftime('%m/%d')} – {sunday.strftime('%m/%d')}"


def get_weekly_report_ids() -> list[str]:
    """Return generated weekly report IDs, newest first."""
    weekly_dir = DOCS_REPORTS_DIR / "weekly"
    report_ids = []
    for path in weekly_dir.glob("*.md"):
        if path.name == "index.md":
            continue
        try:
            get_week_date_range(path.stem)
        except ValueError:
            continue
        report_ids.append(path.stem)
    return sorted(report_ids, reverse=True)


def update_weekly_archive() -> None:
    """Refresh the MkDocs weekly archive page from generated reports."""
    report_ids = get_weekly_report_ids()
    rows = [
        f"| {report_id} | {get_week_date_range(report_id)} | [查看]({report_id}.md) |"
        for report_id in report_ids
    ]
    content = "\n".join(
        [
            "---",
            "title: 周报归档",
            "---",
            "",
            "# 📋 周报归档",
            "",
            "按周归档的项目进度报告。",
            "",
            "| 年份-周 | 日期范围 | 链接 |",
            "|---------|---------|------|",
            *rows,
            "",
            '!!! info "自动生成"',
            "    运行 `make weekly` 可自动生成本周周报草稿。",
            "",
        ]
    )
    (DOCS_REPORTS_DIR / "weekly" / "index.md").write_text(content, encoding="utf-8")


def update_home_recent_reports() -> None:
    """Refresh the homepage recent reports table with the newest weekly report."""
    report_ids = get_weekly_report_ids()
    if not report_ids:
        return

    latest = report_ids[0]
    latest_week = latest.split("-")[1]
    replacement = "\n".join(
        [
            "## 📅 最近汇报",
            "",
            "| 类型 | 期数 | 日期 | 链接 |",
            "|------|------|------|------|",
            f"| 周报 | {latest_week} | {get_week_date_range(latest)} | [查看](reports/weekly/{latest}.md) |",
            "",
        ]
    )

    index_path = PULSE_ROOT / "docs" / "index.md"
    text = index_path.read_text(encoding="utf-8")
    start_marker = "## 📅 最近汇报"
    end_marker = "\n---\n\n## 🏗️ 项目甘特图"
    start = text.find(start_marker)
    end = text.find(end_marker, start)
    if start == -1 or end == -1:
        return
    index_path.write_text(text[:start] + replacement + text[end:], encoding="utf-8")


def update_weekly_indexes() -> None:
    """Refresh all index pages that point to generated weekly reports."""
    update_weekly_archive()
    update_home_recent_reports()


def get_current_month() -> str:
    """返回当前月份，如 '2026-05'。"""
    return datetime.now().strftime("%Y-%m")


def get_month_end(year_month: str) -> str:
    """返回月末日期字符串。"""
    year, month = map(int, year_month.split("-"))
    if month == 12:
        end = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        end = datetime(year, month + 1, 1) - timedelta(days=1)
    return end.strftime("%Y-%m-%d")


def load_collected_data() -> list[dict]:
    """从 .cache/collected_data.json 加载采集数据。"""
    data_file = CACHE_DIR / "collected_data.json"
    if not data_file.exists():
        print(f"⚠️  未找到采集数据 {data_file}")
        print("   请先运行: python scripts/collect.py")
        sys.exit(1)

    with open(data_file, encoding="utf-8") as f:
        return json.load(f)


# ── 渲染函数 ─────────────────────────────────────────────────────


def render_weekly(week_str: str | None = None) -> Path:
    """渲染周报并写入文件。"""
    week_str = week_str or get_iso_week()
    data = load_collected_data()

    template = env.get_template("weekly.md.j2")
    content = template.render(
        week_id=week_str,
        date_range=get_week_date_range(week_str),
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M"),
        projects=data,
        risks=[],
    )

    # 写入 reports/weekly/
    out_dir = REPORTS_DIR / "weekly"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{week_str}.md"
    out_path.write_text(content, encoding="utf-8")

    # 同步到 docs/reports/weekly/ (供 MkDocs 使用)
    docs_out_dir = DOCS_REPORTS_DIR / "weekly"
    docs_out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(out_path, docs_out_dir / f"{week_str}.md")
    update_weekly_indexes()

    print(f"✅ 周报已生成: {out_path}")
    print(f"   同步到 docs: {docs_out_dir / f'{week_str}.md'}")
    return out_path


def render_monthly(month_str: str | None = None) -> Path:
    """渲染月报并写入文件。"""
    month_str = month_str or get_current_month()
    data = load_collected_data()

    # 为月报添加额外字段
    for p in data:
        p["monthly_highlights"] = p.get("highlights", ["无更新"])
        p["weekly_summaries"] = []  # 后续可从各周周报文件提取
        p["next_month_plan"] = "待补充"

    year, month = month_str.split("-")
    template = env.get_template("monthly.md.j2")
    content = template.render(
        year=year,
        month=month,
        month_end=get_month_end(month_str),
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M"),
        projects=data,
        risks=[],
    )

    out_dir = REPORTS_DIR / "monthly"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{month_str}.md"
    out_path.write_text(content, encoding="utf-8")

    docs_out_dir = DOCS_REPORTS_DIR / "monthly"
    docs_out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(out_path, docs_out_dir / f"{month_str}.md")

    print(f"✅ 月报已生成: {out_path}")
    print(f"   同步到 docs: {docs_out_dir / f'{month_str}.md'}")
    return out_path


# ── CLI ──────────────────────────────────────────────────────────


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Pulse – 报告渲染器")
    subparsers = parser.add_subparsers(dest="command", help="报告类型")

    # weekly
    weekly_parser = subparsers.add_parser("weekly", help="生成周报")
    weekly_parser.add_argument("--week", help="ISO 周标识，如 2026-W19")

    # monthly
    monthly_parser = subparsers.add_parser("monthly", help="生成月报")
    monthly_parser.add_argument("--month", help="月份标识，如 2026-05")

    args = parser.parse_args()

    if args.command == "weekly":
        render_weekly(args.week)
    elif args.command == "monthly":
        render_monthly(args.month)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
