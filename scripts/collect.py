#!/usr/bin/env python3
"""
collect.py – 从各项目 repo 收集 git 提交记录和元数据。

用法:
    python scripts/collect.py --since "1 week ago"
    python scripts/collect.py --since "1 month ago" --output data.json
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yaml

try:
    from git import Repo, InvalidGitRepositoryError
except ImportError:
    print("ERROR: gitpython not installed. Run: pip install gitpython", file=sys.stderr)
    sys.exit(1)

try:
    from rich.console import Console
    from rich.table import Table

    console = Console()
except ImportError:
    console = None

# ── 配置 ────────────────────────────────────────────────────────

PULSE_ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR = PULSE_ROOT / "projects"

# 默认扫描 pulse 同级目录
DEFAULT_PROJECTS_ROOT = PULSE_ROOT.parent


STATUS_EMOJI = {
    "active": "🟢",
    "paused": "🟡",
    "completed": "🔵",
    "archived": "⚪",
}


# ── 核心函数 ─────────────────────────────────────────────────────


def discover_projects() -> list[dict[str, Any]]:
    """扫描 projects/ 目录下所有 meta.yaml，返回项目列表。"""
    projects = []
    for meta_path in sorted(PROJECTS_DIR.glob("*/meta.yaml")):
        with open(meta_path) as f:
            meta = yaml.safe_load(f)
        meta["_dir"] = meta_path.parent.name
        meta["_meta_path"] = str(meta_path)

        # 读取里程碑
        ms_path = meta_path.parent / "milestones.yaml"
        if ms_path.exists():
            with open(ms_path) as f:
                ms_data = yaml.safe_load(f)
            meta["_milestones"] = ms_data.get("milestones", [])
        else:
            meta["_milestones"] = []

        projects.append(meta)
    return projects


def get_repo_path(project: dict) -> Path | None:
    """获取项目实际 git repo 路径。"""
    # 优先用 meta.yaml 中指定的 local_path
    local = project.get("local_path")
    if local:
        p = Path(local)
        if p.exists():
            return p

    # fallback: pulse 同级目录下同名文件夹
    p = DEFAULT_PROJECTS_ROOT / project["_dir"]
    if p.exists():
        return p

    return None


def collect_commits(
    repo_path: Path, since: str = "1 week ago"
) -> list[dict[str, str]]:
    """从 git repo 收集指定时间段的提交记录。"""
    try:
        repo = Repo(repo_path)
    except (InvalidGitRepositoryError, Exception):
        return []

    commits = []
    try:
        for commit in repo.iter_commits(since=since, max_count=100):
            commits.append(
                {
                    "hash": commit.hexsha[:8],
                    "date": datetime.fromtimestamp(commit.committed_date).strftime(
                        "%Y-%m-%d %H:%M"
                    ),
                    "message": commit.message.strip().split("\n")[0],
                    "author": str(commit.author),
                }
            )
    except Exception:
        pass

    return commits


def get_active_milestones(milestones: list[dict]) -> list[dict]:
    """返回当前活跃的里程碑。"""
    return [m for m in milestones if m.get("status") == "active"]


def compute_completion(milestones: list[dict]) -> int:
    """计算里程碑完成百分比。"""
    if not milestones:
        return 0
    done = sum(1 for m in milestones if m.get("status") == "done")
    return int(done / len(milestones) * 100)


def collect_all(since: str = "1 week ago") -> list[dict[str, Any]]:
    """收集所有项目的数据。"""
    projects = discover_projects()
    results = []

    for proj in projects:
        repo_path = get_repo_path(proj)
        commits = collect_commits(repo_path, since) if repo_path else []
        active_ms = get_active_milestones(proj["_milestones"])
        completion = compute_completion(proj["_milestones"])

        result = {
            "name": proj["name"],
            "display_name": proj.get("display_name", proj["name"]),
            "status": proj.get("status", "active"),
            "status_emoji": STATUS_EMOJI.get(proj.get("status", "active"), "⚪"),
            "commit_count": len(commits),
            "commits": commits[:10],  # 最多 10 条
            "active_milestones": [
                {
                    "name": m["name"],
                    "start": str(m.get("start", "")),
                    "end": str(m.get("end", "")),
                    "status": m.get("status", ""),
                }
                for m in active_ms
            ],
            "active_milestone_names": ", ".join(m["name"] for m in active_ms)
            or "—",
            "completion_pct": completion,
            "milestones": proj["_milestones"],
            "summary": f"{len(commits)} 次提交" if commits else "本周无提交",
            "highlights": [c["message"] for c in commits[:5]] or ["无更新"],
            "next_week_plan": "待补充",
        }
        results.append(result)

    return results


def print_summary(data: list[dict]) -> None:
    """终端打印摘要（使用 rich）。"""
    if console is None:
        for d in data:
            print(f"  {d['status_emoji']} {d['display_name']}: {d['commit_count']} commits")
        return

    table = Table(title="📊 项目数据采集结果", show_lines=True)
    table.add_column("项目", style="bold cyan")
    table.add_column("状态", justify="center")
    table.add_column("提交数", justify="right")
    table.add_column("完成率", justify="right")
    table.add_column("活跃里程碑")

    for d in data:
        table.add_row(
            d["display_name"],
            f"{d['status_emoji']} {d['status']}",
            str(d["commit_count"]),
            f"{d['completion_pct']}%",
            d["active_milestone_names"],
        )
    console.print(table)


# ── CLI ──────────────────────────────────────────────────────────


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Pulse – 项目数据采集")
    parser.add_argument(
        "--since", default="1 week ago", help="Git log 时间范围 (默认: '1 week ago')"
    )
    parser.add_argument("--output", "-o", help="输出 JSON 文件路径")
    parser.add_argument("--quiet", "-q", action="store_true", help="静默模式")
    args = parser.parse_args()

    data = collect_all(since=args.since)

    if not args.quiet:
        print_summary(data)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n✅ 数据已保存到 {out_path}")
    else:
        # 默认输出到 pulse 根目录
        default_out = PULSE_ROOT / ".cache" / "collected_data.json"
        default_out.parent.mkdir(parents=True, exist_ok=True)
        with open(default_out, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        if not args.quiet:
            print(f"\n✅ 数据已保存到 {default_out}")

    return data


if __name__ == "__main__":
    main()
