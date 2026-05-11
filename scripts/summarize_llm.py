#!/usr/bin/env python3
"""
summarize_llm.py – 使用本地 vLLM (OpenAI 兼容接口) 将 git commit 信息摘要为中文进度。

默认不启用，需 USE_LLM=1 环境变量。

用法:
    USE_LLM=1 python scripts/summarize_llm.py
    USE_LLM=1 python scripts/summarize_llm.py --input .cache/collected_data.json
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

PULSE_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = PULSE_ROOT / ".cache"

# ── 配置 ────────────────────────────────────────────────────────

VLLM_BASE_URL = os.environ.get("VLLM_BASE_URL", "http://localhost:8000/v1")
VLLM_MODEL = os.environ.get("VLLM_MODEL", "Qwen/Qwen3-8B")

SYSTEM_PROMPT = """你是一个项目进度摘要助手。给你一组 git commit 信息，请用中文简洁地总结本周的工作进展。
要求：
1. 用 3-5 个要点概括，每条不超过 20 字
2. 只输出要点列表，不要多余解释
3. 用 "- " 开头"""


def is_enabled() -> bool:
    """检查是否启用 LLM 摘要。"""
    return os.environ.get("USE_LLM", "0") == "1"


def summarize_commits(commits: list[dict]) -> list[str]:
    """调用 vLLM 将 commit 列表摘要为中文要点。"""
    try:
        import requests
    except ImportError:
        print("ERROR: requests not installed.", file=sys.stderr)
        return []

    if not commits:
        return ["无更新"]

    # 构造 commit 文本
    commit_text = "\n".join(
        f"- [{c.get('date', '')}] {c.get('message', '')}" for c in commits
    )

    try:
        resp = requests.post(
            f"{VLLM_BASE_URL}/chat/completions",
            json={
                "model": VLLM_MODEL,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": f"以下是本周的 git commit 记录，请总结：\n\n{commit_text}",
                    },
                ],
                "max_tokens": 256,
                "temperature": 0.3,
            },
            timeout=60,
        )
        resp.raise_for_status()
        result = resp.json()
        content = result["choices"][0]["message"]["content"].strip()

        # 解析要点
        lines = [
            line.strip().lstrip("- ").strip()
            for line in content.split("\n")
            if line.strip().startswith("-")
        ]
        return lines if lines else [content]

    except Exception as e:
        print(f"⚠️  LLM 调用失败: {e}", file=sys.stderr)
        return [c.get("message", "") for c in commits[:5]]


def enrich_data(data: list[dict]) -> list[dict]:
    """为采集数据添加 LLM 生成的摘要。"""
    for proj in data:
        commits = proj.get("commits", [])
        if commits:
            summary_lines = summarize_commits(commits)
            proj["highlights"] = summary_lines
            proj["summary"] = "; ".join(summary_lines[:3])
            print(f"  ✅ {proj['display_name']}: {len(summary_lines)} 条摘要")
        else:
            proj["highlights"] = ["无更新"]
            proj["summary"] = "本周无提交"
    return data


def main():
    if not is_enabled():
        print("ℹ️  LLM 摘要未启用。设置 USE_LLM=1 以启用。")
        print("   例: USE_LLM=1 python scripts/summarize_llm.py")
        sys.exit(0)

    import argparse

    parser = argparse.ArgumentParser(description="Pulse – LLM 摘要生成")
    parser.add_argument(
        "--input",
        default=str(CACHE_DIR / "collected_data.json"),
        help="输入 JSON 文件",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ 文件不存在: {input_path}")
        print("   请先运行: python scripts/collect.py")
        sys.exit(1)

    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)

    print(f"🤖 正在调用 LLM ({VLLM_MODEL}) 生成摘要...")
    data = enrich_data(data)

    # 写回
    with open(input_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 摘要已更新到 {input_path}")


if __name__ == "__main__":
    main()
