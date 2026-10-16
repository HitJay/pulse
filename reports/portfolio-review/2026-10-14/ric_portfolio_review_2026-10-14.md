# RIC 卡片组合复盘：前沿方向与新项目建议

> 已被 v2 取代：`ric_portfolio_review_2026-10-14_v2.md`（对齐 2026 Goal + NNRCC Operational Model）。本文保留作对照。

- 日期：2026-10-14
- 范围：Jira 中 QYJI 为 assignee 或 reporter 的全部卡片（52 张，RIC 51 + DBIO 1）
- 数据快照：同目录 `jira_snapshot.csv` / `jira_snapshot.json`（由 `scripts/portfolio-review/snapshot_jira.py` 生成，可复跑）
- 性质：内部自用规划文档（中文）。对外/上 Jira 时需改写为英文，并按惯例隐去真实靶点与供应商名。
- 标注约定：FACT = Jira/文献可查证；OBS = 我对卡片内容的观察；HYP = 建议/判断，未经验证。

---

## 1. 现状：四条工作线

| 线 | 卡片 | 一句话定位 |
|---|---|---|
| A 影像 / HCS 管线 | RIC-247, 261, 394, 375, 358, 209, 331, 305, 390, 342, 379, 217 | 单 assay 管线成熟，多批次落地 |
| B 虚拟细胞 / vAssay | RIC-381, 298, 254, 300, 312 | 381 已做到 DRUG-seq × DINOv2 × TMRM × ATP 四模态、N=175 |
| C 安全性评估工具 | RIC-349, 391, 395, 404, 364, 400, 405, 386, 385, 398, 387 | v1.4.x，305 门回归，Shiny intake，Portal 文档 |
| D 成药性 Agent | RIC-403, 407, 392/393, 396, 384, 388, 389 | 结构 / 对接 / 分子胶 / 肽 / BBB |

OBS：四条线的产出最终都是"某个靶点的一组证据"，但目前分散在 4 个 repo、几十张卡里，相互没有打通。这是本文后面所有建议的出发点。

状态分布（FACT，2026-10-14）：In Progress 22 · Review 13 · Done 15 · Analysis 1 · Forwarded 1。

---

## 2. 看板卫生（低成本、先做）

### 2.1 Review 积压（FACT）

| 卡片 | 停留天数 | 建议 |
|---|---|---|
| RIC-244 / 245 / 246（Campaign #22/#24/#31 TMRM） | 146 | 内容已并入 RIC-381，可走 Done，Conclusion 指向 381 |
| RIC-262（O-304）、RIC-270（FA/TG DOE）、RIC-331（2-channel TMRM）、RIC-218（STOmics） | 146 | 找 reviewer 一次性过；无后续则 Done |
| RIC-384（MC4R BBB） | 139 | 后续已在 388/389，Done |
| RIC-261（Myotube BP v2.0.0） | 64 | 应用侧已分到 RIC-394，催 review 关闭 |
| RIC-392 / 393 | 27 | 标题完全相同，疑似重复卡，合并或关闭一张 |
| RIC-400 / 405 | 27 | 正常 review 周期 |

### 2.2 长期停滞的 In Progress（FACT，>90 天无更新）

RIC-209 / 217 / 254（517 天）、RIC-292（467）、RIC-247（195）、DBIO-455（183）、RIC-298 / 390 / 386（128）、RIC-358（126）、RIC-388（119）、RIC-364（96）。

建议（HYP）：
- 209 / 217 / 254 / 292：先确认是否还在做。不做的走 Closure 流程（重写 Description，再填 Done 门禁三字段）；还在做的补一条现状 comment。
- 247 是基础设施的常驻卡，保留，但补一条近况。
- DBIO-455 不在 RIC 板，确认归属后关闭。

### 2.3 旗舰卡状态不符

RIC-381 是目前最活跃的项目，却仍停在 Analysis，Description 还是空模板（FACT）。建议转到 In Progress，并补齐 Description（Background / Modalities / N / Data paths / Related tickets）。

---

## 3. 各条线的前沿建议

### B. 虚拟细胞（RIC-381）——优先级最高

1. 从"刻画"走到"预测"（HYP）。业界所说的 virtual cell（如 Arc Institute 的 Virtual Cell Challenge / State 模型、scGPT、CellFlow 一类），核心检验标准是能否预测未测过的扰动。381 目前回答的是"各模态读出什么、哪里一致"。下一步建议：
   - 留出部分靶点作为 held-out，用 DRUG-seq signature 预测这些靶点的 TMRM / ATP 表型
   - 报告预测相关性，并与 NTC 置换基线比较

   做到这一步，才能被称为 virtual cell，而不只是一份 characterization 报告。

2. 用公共数据弥补 N=175 偏小的问题。
   - FACT：Nadig, Replogle et al. 在 HepG2 中做了 essential-gene CRISPRi Perturb-seq（2,393 个扰动，中位数约 45 cells/扰动），见 "Transcriptome-wide characterization of genetic perturbations"（PMC11244993 / PMC13063516）。它与 381 是同一细胞系，可用于外部一致性检验（overlap 靶点的 signature 相关性）或迁移预训练。
   - 注意：该数据是 CRISPRi 而非 siRNA，且只覆盖 essential 基因，与 381 的 overlap 需要先算一下。
   - 影像侧可参考 JUMP-CP（ORF/CRISPR Cell Painting）和 Recursion 的 RxRx3-core / OpenPhenom（公开状态需自行核实）。

3. 采用社区 benchmark（HYP）。参考 Recursion 的 EFAAR 思路：检验扰动 embedding 能否召回 CORUM / STRING / Reactome 中已知的蛋白关系。这比自定义指标更有说服力，也更容易对外沟通。

4. 视觉 embedding（HYP）。DINOv2 是通用模型，建议与细胞专用模型做一次 A/B 对比（如 SubCell、CHAMMI 系列、OpenPhenom），并补上 TVN / sphering 跨批次校正（以 NTC 为参照）。

5. 兑现标题中的 "data Fairness"（HYP）。影像转 OME-Zarr，配一个元数据目录（plate / well / siRNA / batch / modality）。这样也能顺带缓解 CIFS 并发读锁的问题。

### C. 安全性评估工具（RIC-349 系）

1. 关键词计分是天花板（OBS）。RIC-400（PEX16，句子级否定导致严重漏判为 GREEN）暴露的就是这一点。前沿做法（HYP）：
   - 由 LLM 做结构化断言抽取：风险是否成立、方向、证据原句，再自动校验引用原文是否真实存在
   - 用这一层替代或校正关键词分

   当前路线图把它定为"phase 4，延后"，建议提前做，因为这是质变而非小修。

2. 补确定性的结构化证据层（HYP）：
   - gnomAD LOEUF / pLI
   - IMPC 小鼠敲除表型
   - Open Targets safety liabilities
   - DepMap essentiality
   - GTEx / HPA 组织表达

   与 LLM 判断加权融合，并且每一项都可追溯。

3. 校准与弃权（HYP）。305 门目前只报准确率。建议增加：风险分校准曲线（reliability diagram）、"证据不足 / abstain"输出，以及 abstain 率与准确率的权衡曲线。

### D. 成药性 Agent（RIC-403 / 407 等）

1. 数值可信度（OBS → 风险）。卡片里出现了 ΔG = −21.49 kcal/mol（RIC-403）、"86 µM → 3.85 mM"（RIC-407）这类数字，它们来自 PRODIGY 等打分函数的估计，不是实测亲和力。建议：
   - 对外一律标为相对排序或 HYP
   - 选 5–10 个有实验 Ki / IC50 的已知配体，画打分 vs 实验的校准散点图，写进 Agent 的 benchmark

2. 生成式设计（HYP，需要湿实验伙伴）。从"给已有分子打分"升级到"生成候选"：BindCraft / RFdiffusion 生成肽结合剂，再用 Boltz-2 / AF3 交叉筛选。适合 OXTR、GLP-1R 这类肽靶点。没有湿实验伙伴承诺验证前，不建议立项。

### A. 影像管线

1. 用自监督 embedding 替代手工特征（HYP），与 B 线共用同一 embedding 服务，把 TMRM / 肌管 / 脂解 / Seahorse 放进同一个跨 assay 表型空间。
2. 把 QC 前移（HYP）：在 RIC-342 离群检测的基础上，做成每块板入库时自动跑的 QC，结果写入 batch registry。

---

## 4. 新项目候选（按 ROI 排序）

| # | 项目 | 做法 | 价值 | 可行性 / 依赖 | 建议挂卡 |
|---|---|---|---|---|---|
| 1 | 干湿一致性验证：安全工具预测 vs HepG2 体外毒性 | 对 381 的 175 个靶点跑安全工具，与 ATP / TMRM 毒性信号做一致性分析（混淆矩阵、秩相关） | 首次用自有湿实验数据外部验证安全工具，同时给 381 明确的用途 | 数据齐全，约 1–2 周，无外部依赖 | 新 Capability 卡，关联 349 + 381 |
| 2 | 统一靶点档案 Agent | 输入一个基因，汇总 safety + druggability + BBB + virtual-cell 表型 + 遗传学（pQTL / PheWAS），输出一页带出处的档案；入口复用 RIC-395 Shiny 表单 | 把四条线合成一个对外产品 | 季度级；先定 schema 与接口，再逐模块接入 | 新 Capability 卡 |
| 3 | 前瞻性预测与公开对答案 | 下一个 TDE campaign 开跑前，先用 381 模型预测新靶点表型并存档（hash + 日期），出数后对比 | 建立 virtual cell 可信度最直接的方式 | 成本极低；依赖 campaign 排期 | 作为 381 的里程碑 |
| 4 | 主动学习选靶（lab-in-the-loop） | 按模型不确定性推荐下一轮 siRNA 优先测哪些靶点 | 模型反哺实验 | 实验设计须由生物团队主导，计算侧只提供排序 | 视 #3 结果再定 |
| 5 | 跨 assay 表型图谱 + FAIR 影像目录 | 统一 embedding，配合 OME-Zarr 元数据目录 | 兑现 381 的 Fairness 目标，A / B 线共用 | 中等；存储与 CIFS 约束需评估 | 并入 381 或 247 |
| 6 | 遗传学因果层 | 在 pQTL 基础上增加 GWAS 共定位与孟德尔随机化 | 对有人类遗传支持的靶点（如 RIC-407）直接有用 | 中等；OTv4 + 公共 GWAS summary stats | 并入 #2 的一个模块 |

---

## 5. 建议节奏

1. 第 1 周：看板卫生（§2）。完成 Review 积压清理、停滞卡定性、381 状态与 Description 修正、392 / 393 去重。
2. 第 2–3 周：项目 #1（干湿一致性验证）。
3. 第 4 周起：在 381 中加入 held-out 预测（§3-B-1）和前瞻性预测存档（#3）。
4. 本季度：项目 #2 立项，先出 schema 与 MVP（safety + druggability 两模块）。
5. #4 / #5 / #6 视资源和 #1、#3 的结果再定。

---

## 6. 局限与假设

- 本复盘基于卡片的 summary / description 和最近几条 comment，没有逐卡阅读全部评论与代码，个别卡片的真实进度可能比 Jira 显示的更新。
- §3 中的外部模型和数据集名称为领域常识性引用。除 Nadig/Replogle HepG2 Perturb-seq 已检索确认外，其余（State、OpenPhenom、SubCell、BindCraft 等）的最新版本与可获取性需在立项时逐一核实。
- 所有 HYP 条目均为方向建议，具体湿实验设计不在本文范围内。

## 7. 复跑

```bash
cd /das/user/QYJI/pulse
python3 scripts/portfolio-review/snapshot_jira.py reports/portfolio-review/$(date +%F)
```
