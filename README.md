# 🎯 Pulse – 项目管理仪表盘

[![Docs](https://img.shields.io/badge/docs-online-blue?logo=materialformkdocs)](https://hitjay.github.io/pulse)
[![License](https://img.shields.io/badge/license-private-lightgrey)]()

> **多项目进度管理 · 自动化周报/月报 · 一键 PPT 生成**

Pulse 是一个基于 Markdown 的项目管理中枢，提供：

- 🌐 **文档站**（MkDocs Material）— 对内浏览、搜索、甘特图
- 📋 **自动化报告** — 从各 repo 的 git log 自动采集，Jinja2 模板渲染
- 📊 **PPT/PDF 一键生成** — Marp CLI 或 python-pptx 出幻灯片，直接给领导
- 🤖 **可选 LLM 摘要** — 接本地 vLLM (Qwen3-8B) 把 commit messages → 中文摘要
- ⚙️ **GitHub Actions** — push 自动部署文档站，每周一自动开周报 PR

---

## 📁 项目结构

```
pulse/
├── docs/                    # MkDocs 内容根（文档站页面）
│   ├── index.md             # 总览仪表盘
│   ├── projects/            # 各项目详情页
│   └── reports/             # 周/月/季报（同步自 reports/）
├── projects/                # 项目元数据（结构化 YAML）
│   └── 3_safety/
│       ├── meta.yaml        # 项目信息、状态、标签
│       ├── milestones.yaml  # 里程碑（驱动甘特图+完成率）
│       └── progress.md      # 时间线笔记
├── reports/                 # 生成的报告源文件（Marp 格式）
│   ├── weekly/
│   └── monthly/
├── decks/                   # 生成的 PPT/PDF（gitignored）
├── templates/               # Jinja2 模板
├── scripts/                 # 自动化脚本
│   ├── collect.py           # 采集各 repo git log + meta
│   ├── render.py            # 渲染周/月报 Markdown
│   ├── summarize_llm.py     # LLM 摘要（默认 OFF）
│   └── build_deck.py        # Markdown → PPTX/PDF
├── mkdocs.yml               # 文档站配置
├── Makefile                 # 一键命令
└── .github/workflows/       # CI/CD
    ├── docs.yml             # push → 自动部署文档站
    └── weekly.yml           # 每周一 → 自动开周报 PR
```

---

## 🚀 快速开始

### 1. 安装依赖

```bash
cd pulse
pip install -e ".[dev]"

# 可选：安装 marp-cli（用于生成 PPT/PDF）
npm install -g @marp-team/marp-cli
```

### 2. 预览文档站

```bash
make serve
# 浏览器打开 http://localhost:8000
```

### 3. 生成周报

```bash
make weekly                    # 自动采集 + 生成本周周报
make weekly WEEK=2026-W19      # 指定周
```

### 4. 生成 PPT

```bash
make deck WEEK=2026-W19        # PPTX
make deck-pdf WEEK=2026-W19    # PDF
```

### 5. 部署文档站

```bash
make deploy                    # 推送到 GitHub Pages
```

---

## 📖 命令速查

| 命令 | 说明 |
|------|------|
| `make help` | 显示所有可用命令 |
| `make install` | 安装 Python 依赖 |
| `make serve` | 本地预览文档站 |
| `make collect` | 从各项目采集 git 数据 |
| `make weekly` | 生成本周周报 |
| `make monthly` | 生成本月月报 |
| `make deck` | 生成 PPT 幻灯片 |
| `make deck-pdf` | 生成 PDF 幻灯片 |
| `make deploy` | 部署到 GitHub Pages |
| `make all` | 采集 + 周报 + PPT 一条龙 |
| `make clean` | 清理生成文件 |

---

## 📂 添加新项目

1. 在 `projects/` 下创建新目录：

```bash
mkdir projects/2_myotube
```

2. 创建 `meta.yaml`：

```yaml
name: 2_myotube
display_name: 肌管分析
description: 肌管图像分析流水线
owner: QYJI
status: active
local_path: /home/QYJI/das/2_myotube
start_date: 2026-06-01
target_end_date: 2026-12-31
tags: [imaging, cell-biology]
```

3. 创建 `milestones.yaml`（可选）和 `progress.md`

4. 在 `docs/projects/` 添加对应页面，更新 `mkdocs.yml` 的 nav

---

## 🤖 LLM 摘要（可选）

默认关闭。启用方式：

```bash
# 确保 vLLM 服务运行中
USE_LLM=1 make weekly
```

配置 `.env`：

```bash
VLLM_BASE_URL=http://localhost:8000/v1
VLLM_MODEL=Qwen/Qwen3-8B
```

---

## ⚙️ GitHub Actions

| Workflow | 触发条件 | 功能 |
|----------|---------|------|
| `docs.yml` | push 到 main（docs/ 或 mkdocs.yml 变更） | 自动构建并部署文档站到 GitHub Pages |
| `weekly.yml` | 每周一 09:00 (UTC+8) 或手动触发 | 自动采集数据、生成周报、开 PR |

首次使用需在 GitHub repo Settings → Pages 中设置 Source 为 `gh-pages` 分支。

---

<small>Built with ❤️ using MkDocs Material + Marp + Python</small>
