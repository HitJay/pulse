# ╔════════════════════════════════════════════════════════════════╗
# ║  Pulse – 项目管理仪表盘                                       ║
# ║  make <target> 一键操作                                       ║
# ╚════════════════════════════════════════════════════════════════╝

.PHONY: help install serve build deploy weekly monthly quarterly deck collect summarize clean

# 默认目标
help: ## 显示帮助
	@echo ""
	@echo "  🎯 Pulse – 可用命令"
	@echo "  ════════════════════════════════════════"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ""

# ── 环境 ────────────────────────────────────────────────────────

install: ## 安装 Python 依赖
	pip install -e ".[dev]"
	@echo ""
	@echo "💡 可选: npm install -g @marp-team/marp-cli  (用于生成 PPT/PDF)"

# ── 文档站 ───────────────────────────────────────────────────────

serve: ## 本地预览文档站 (http://localhost:8000)
	mkdocs serve -a 0.0.0.0:8000

build: ## 构建静态文档站
	mkdocs build

deploy: ## 部署到 GitHub Pages
	mkdocs gh-deploy --force

# ── 数据采集 ─────────────────────────────────────────────────────

SINCE ?= 1 week ago

collect: ## 从各项目 repo 采集数据 (SINCE="1 week ago")
	python scripts/collect.py --since "$(SINCE)"

collect-month: ## 采集最近一个月的数据
	python scripts/collect.py --since "1 month ago"

summarize: ## [可选] 用 LLM 生成中文摘要 (需 USE_LLM=1)
	USE_LLM=1 python scripts/summarize_llm.py

# ── 报告生成 ─────────────────────────────────────────────────────

WEEK ?= $(shell python -c "from datetime import datetime; d=datetime.now(); print(f'{d.isocalendar()[0]}-W{d.isocalendar()[1]:02d}')")
MONTH ?= $(shell date +%Y-%m)

weekly: collect ## 生成本周周报 (WEEK=2026-W19)
	python scripts/render.py weekly --week $(WEEK)
	@echo ""
	@echo "📋 周报已生成: reports/weekly/$(WEEK).md"
	@echo "   预览: make serve"
	@echo "   出 PPT: make deck WEEK=$(WEEK)"

monthly: collect-month ## 生成本月月报 (MONTH=2026-05)
	python scripts/render.py monthly --month $(MONTH)
	@echo ""
	@echo "📊 月报已生成: reports/monthly/$(MONTH).md"

quarterly: ## 生成季报 (TODO)
	@echo "🚧 季报生成功能开发中..."

# ── 幻灯片 ───────────────────────────────────────────────────────

deck: ## 生成 PPT (WEEK=2026-W19 或 MONTH=2026-05)
ifdef MONTH_DECK
	python scripts/build_deck.py monthly $(MONTH_DECK)
else
	python scripts/build_deck.py weekly $(WEEK)
endif
	@echo ""
	@echo "📁 输出目录: decks/"

deck-pdf: ## 生成 PDF 幻灯片
ifdef MONTH_DECK
	python scripts/build_deck.py monthly $(MONTH_DECK) --pdf
else
	python scripts/build_deck.py weekly $(WEEK) --pdf
endif

# ── 清理 ─────────────────────────────────────────────────────────

clean: ## 清理生成文件
	rm -rf site/ .cache/ decks/*.pptx decks/*.pdf
	@echo "🧹 已清理"

# ── 一键全流程 ────────────────────────────────────────────────────

all: weekly deck ## 采集 + 生成周报 + 出 PPT
	@echo ""
	@echo "🎉 全部完成！"
	@echo "   周报: reports/weekly/$(WEEK).md"
	@echo "   PPT:  decks/$(WEEK).pptx"
	@echo "   预览: make serve"
