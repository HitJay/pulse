# RIC 卡片组合复盘 v2（当前 v2.4）：对齐 2026 Goal 与 NNRCC Operational Model

- 日期：2026-10-14（v2；v1 = `ric_portfolio_review_2026-10-14.md`，保留作对照）
- v2 变更：用 monthly_report 目录里的 scope 文件重新校准 v1 的建议——每个项目挂到 Goal 编号与 FTE，对齐 Highway / Red line 运营模式。
- v2.1（同日）：按 QYJI 决定，不再以现有平台（Drug Target Research AI platform / QTL-GWAS Explorer / assay-insights / AI 蛋白组学）为约束，靶点档案 Agent 与遗传学因果层均自建。
- v2.2（同日）：逐页重读 [OPS] 的 Highway 部分（slide 4–14，包括表格、分组形状和审阅批注），新增 §1b，并据此细化 P3 / P4 / P7。
- v2.3（同日）：新增 §7「探索性增长点」。先检索前沿文献（链接见 §7.0），再筛出高影响、高潜力且能利用自有数据或流程优势的方向。
- v2.4（同日）：E2 改为优先使用无需申请权限的公开数据，数据源已在 hpccnrd001 上实测可达（见 E2 数据层）。
- 性质：内部规划（中文，含内部靶点名与组织信息）。勿 push 到外部 GitHub；对外前需英文化并脱敏。
- 标注：FACT = 来源文件可查证（附出处）；OBS = 观察；HYP = 建议，未验证。

## 0. 引用的 scope 来源

均位于 `R:\DT\TDE_TV\shared_folder\QYJI\monthly_report\`：

| 简称 | 文件 | 用到的内容 |
|---|---|---|
| [GOAL] | legacy/2026_Goal_QYJI.pptx（v3，2026-05-11） | G1–G8 定义与 FTE，经理批注 |
| [OPS] | NNRCC Operational Model Updates.pptx（2026-07） | 三通道、Red line 六条、Highway 六个 MOA cluster、2030 目标 |
| [TH] | 20260625 Mid year review townhall.pdf | Highway 时间线（Pilot 至 12-31，之后全面运行） |
| [1on1] | mid_year_review_1on1_lingling.html | H1 证据与 H2 优先级 |
| [JUL] / [AUG] | NNRCC monthly report July / August 2026.pdf | EE campaign 收尾、AI 平台、QTL-GWAS Explorer、AI 蛋白组学 |
| [AIDR25] | legacy/AIDR_Goals_2025.pptx | AIDR 3.2：3 个 AI vAssay 进 TDE campaign；3.4：MLOps |

---

## 1. 关键 scope 事实（据此修正 v1）

1. 组织目标是从挑选靶点转向去风险（FACT [OPS] [TH]）。2030 winning scenario 是从约 5 个 PreG/年提升到约 30 个，PoS 约 20%。原话是 "Adopting a drug hunter's mindset — SELECT and DERISK (stop/go)" 和 "stick to the HYPOTHESIS, not the TARGET"。
   → 我的工具应以"帮 TC 做 stop/go"为价值叙事，而不是"多一个分析"。

2. 安全工具已写进 Red line（FACT [OPS] slide 5）。第 5 条 Safety 原文是 "Non-RED as evaluated by the Safety Landscape Tool"，请求入口署名 QYJI（[JUL] p13）。我本人是 Individual target working group 成员（organiser YLV，[OPS] slide 3）。
   → 安全工具已经是运营流程中的门禁，不再只是评估项目。它的准确率、校准和周转时间直接影响 Highway 的通量。这是 v1 最大的低估。

3. Highway 节奏（FACT [OPS] slide 6–8，[TH] p41）：
   - 6 个 MOA cluster，每个 cluster 每月一轮。
   - "each department defines standardized highway validation, capacity and running process"
   - Pilot 运行至 12-31，之后进入全面运行。
   - 表达阈值通过 RCCOmics / assay-insights 查询（BKNM0127 SkM：siRNA inhibition 要求 TPM > 30 等）。
   - 其中 SkM Atrophy/Hypertrophy（IGWU/YLV）、SkM FAO/Seahorse、Adipocyte Lipolysis 都是我现有影像管线覆盖的 assay（RIC-261/394、375、390）。

4. 我的 FTE 分配（FACT [GOAL] v3）：

   | Goal | 内容 | FTE |
   |---|---|---|
   | G1 | Assay & Campaign，含接手 NYGZ 的 4 个 assay | 0.30 |
   | G5 | Imaging pipeline & BP | 0.20 |
   | G3 | Safety Landscape Tool，含约 1000 靶点压测 | 0.15 |
   | G4 | Model Characterization | 0.10 |
   | G6 | Assay Data Fairness & ELN | 0.10 |
   | G2 | Individual target | 0.05 |
   | G7 | Human cohort | 0.05 |
   | G8 | Training | 0.05 |

   → 一半时间在 assay / 影像（G1 + G5）。v1 把重心放在 virtual cell 和新 Agent 上，与 FTE 不符。

5. 组织内已有的相关平台（FACT，仅作背景；按 v2.1 决定不作为约束，自建）：
   - Drug Target Research AI platform（FNGQ、EJNH、IJDN、QYJI）：用于 EE Tier-2 hit 优先级 [JUL]
   - AI-assisted proteomics，38 个 AI search module（GMTG、FNGQ）[AUG]
   - QTL-GWAS Explorer（eQTL/pQTL/sQTL/txQTL/metabQTL，TFWG、YUXM）[AUG]
   - assay-insights 表达查询 dashboard（IJDN、TFWG）[JUL] [OPS]

   → v2.1 决定：自建。理由是这些能力要深度嵌进自己的安全工具、影像数据与 Red line 流程，掌控 schema、迭代节奏和审计链；外部平台仅作可选的交叉核对数据源。

6. 经理和 1:1 反馈（FACT [GOAL] notes，[1on1]）：
   - H2 要 "fewer high-impact use cases"、"reusable documented workflows"、"fewer fragmented asks"
   - G5 写明 "refrain from engaging in omics data-related work"
   - 2025 批注 "vAssay no activity next year"；G4 改名为 Model Characterization
   - G8 的正式课程或会议还没完成

7. 管线现状（FACT [AUG] [JUL]）：
   - EE campaign 已完成；core team 背书 AAV-Cas9 in vivo 筛选。
   - PDE3B 于 08-19 进 PreG；GRB10 于 6 月进 PreG。
   - Front-runner：FNIP1、IGF2-Sema、ACOX1、LGALS8、GPR176、SEMA6C。
   - 进行中的是 #6 Insulin sensitization campaign，对应 pAKT / glucose assays。

---

## 1b. Highway 模式细节（FACT，均出自 [OPS]）

### 入口与分流（slide 4–6）
- 靶点假说先过 Red line（自评）。不通过则 stop；通过后由 TC 选择 Highway 或 Classic-way。
- Highway：无需审批，先到先得，不做定制。Classic-way：需 core team 批准资源与方案。
- 进入 in vitro Highway 还需满足三条：
  - 靶点在相关 assay 细胞中的表达超过阈值
  - 只选一个 leading MOA（一个靶点只能测一个治疗方向上的一个假说）
  - 工具分子通过内部 QC
- 不通过则 stop，或转 Classic-way。

### 实验规则（slide 6）
- siRNA：1 个 pool、1 个剂量，跑一轮。
  - 结果 positive：先核实 KDE，重复一次，再交 data package。
  - KDE 不合格：换 1 个 siRNA/sgRNA 再测。
- Protein / peptide：每个靶点最多 3 条序列，2 个剂量。
- 小分子：必须是临床阶段化合物，2 个剂量。
- 结果 negative 即 stop。每个 MOA 预设 3–5 个 assay cluster。

### 六个 MOA cluster 与 assay owner（slide 7，每个 cluster 每月一轮）

| MOA cluster | Primary assay（owner） | Secondary assay（owner） |
|---|---|---|
| Insulin sensitivity & gluconeogenesis | PHH pAKT（ILYH/LYA）、Adipocyte pAKT（HCNG/YLV）、SkM pAKT（CZXU/YQWU/YBYI）、PHH glucose production（EQYU/LYA） | — |
| Insulin sensitivity & glucose uptake | 同上三个 pAKT；Adipocyte glucose uptake（NYOL/YCOL/UHYG）或 SkM glucose uptake（YQWU/YBYI） | — |
| Energy expenditure | PHH FAO（EQYU/LYA/FNGQ/TWQY）、Adipocyte FAO（HCNG/YLV/FNGQ/TWQY）、SkM FAO（IGWU/YBYI/FNGQ/TWQY） | — |
| Lipolysis | Adipocyte lipolysis（OFGM/UHYG） | 若 positive：Adipocyte FAO（HCNG/YLV）、Adipocyte futile cycling（WGHA/UHYG） |
| Muscle preservation | SkM atrophy、SkM hypertrophy（IGWU/YLV） | 若 positive：SkM FAO（IGWU/YBYI/FNGQ/TWQY）、SkM glucose uptake（YQWU/YBYI） |
| Beta cell preservation | ProINS:INS、GSIS、viability（GLTx 外包；XNYG/HQGH/XOS/IYMC，IJYD/SXQ/JXDL） | — |

### 表达阈值（slide 8 人源，slide 13 小鼠）

| 细胞 | assay | 参考数据集 | RNA 阈值 | 蛋白阈值 |
|---|---|---|---|---|
| Beta cell | ProINS:INS / GSIS / viability | BKNM0060（Control_Tunicamycin_2 & 3） | TPM ≥ 1 | > 0 |
| Hepatocyte | FAO / glucose production | BKNM0065 | TPM ≥ 1 | > 0 |
| SkM | Atrophy / hypertrophy；glucose uptake / pAKT | BKNM0127（siNTC.veh） | siRNA 抑制：TPM > 30；激活：TPM > 10 | > 0 |
| SkM | FAO / Seahorse | BKNM0117（T7056_Diff_Ctrl） | 同上 | > 0 |
| Adipocyte | Futile cycling | BKNM0103 | TPM ≥ 1 | > 0 |
| Adipocyte | 其他 adipocyte assay | BKNM0121 | TPM ≥ 1 | > 0 |
| 小鼠（in vivo） | 跨组织 bulk | RCCOmics_BKNM0140 | TPM/CPM > 0 | DIO 小鼠组织蛋白组：排名 < 8000 且 unique peptides ≥ 2 |

### In vivo Highway 与配套资源（slide 9–14）
- 蛋白供给：每个靶点最多 3 条序列，每个 slot 最多 6 条；纯度 75%；每月第 1 和第 3 个周一提交；周期 8 周。
- rAAV（ZYGS）与 HGD（GJSN）DIO 研究：
  - 每季度一个 slot，每批 n=7 个靶点；新设施 Q2 2027 投用后增至 n=14。
  - 周期：rAAV 4–6 个月，HGD 约 11–17 周。
  - 申请需提交一页 one-pager：适应症、假设 MoA（EE / FI / IR / beta cell）、扰动方式（在哪个组织敲低、用哪条序列过表达）。
- 分析读出：BW / FI / 体成分 / HOMA-IR，阳性则加做 oGTT；proteomics 通路分析由 WCWA 出标准报告。

### 审阅批注里的未决点（slide comments）
- in vitro Highway 只覆盖 T2D / obesity 的 assay。批注明确 CVD、MASH 资源不足，走 Classic-way。
- 有人认为吞吐量太低；protein 序列数（3 还是 2）、剂量数（2 还是 3）仍有争议。
- 有人问到人源组织 / 细胞的表达数据；"Who delivers samples"、"Do we have standardized design" 未答复。
- 结论：Highway 规则仍在 pilot 期调整，下游工具要做成规则可配置。

### 对我工作的含义（OBS → HYP）
1. 我负责影像的 assay 在 Highway 中的位置：
   - Muscle preservation 的 primary（SkM atrophy / hypertrophy，RIC-261/394）
   - Muscle preservation 的 secondary（SkM FAO / Seahorse，RIC-375）
   - Lipolysis 的 primary（RIC-390）
   - 这几个 assay 每月一轮，结果直接决定 stop 还是继续。
2. Highway 的结论是二元的：positive → 核实 KDE、重复、交 data package；negative → stop。
   → 影像管线需要预先定义 hit-call 规则（以 NTC 为参照的效应量 / SSMD 阈值，加 KDE 校验字段），不能每批次再人工判断。
3. Red line、进入条件、表达阈值、Classic-way 排除条件都写得很明确，可以机器化。
   → 适合 P4 自动预检，并能自动起草 in vivo one-pager。
4. In vivo slot 每季度只有 7 个，是瓶颈。
   → 对 in vitro positive 靶点做证据排序（安全、遗传方向、成药性、表型一致性）有直接价值。

---

## 2. v1 → v2 的修正

| v1 建议 | v2 处理 | 理由 |
|---|---|---|
| B 线（virtual cell）列为优先级最高 | 降为 G4 范围内的定向任务 | G4 只有 0.10 FTE，且已改名 Model Characterization；EE campaign 已收尾，HepG2 TMRM 短期内没有新的前瞻数据 |
| #1 干湿一致性验证 | 保留并升级为 Red line 第 5 条的验证 | 安全工具已成门禁；用 175 个靶点的 ATP/TMRM 做外部验证，正好回答"Non-RED 门槛是否可信" |
| #2 统一靶点档案 Agent | 保留并自建，第一个落地场景定为 Red line 预检（见 P4） | Red line 是明确、高频、我已在其工作组的场景；自建以掌控 schema 和审计链 |
| #3 前瞻性预测 | 保留但降级，等待合适的 campaign | 当前 #6 campaign 是 pAKT 读出，不是 HepG2 TMRM |
| #4 主动学习选靶 | 移除（本年度） | 无 FTE；实验设计由生物团队主导 |
| #5 跨 assay 图谱 + FAIR 目录 | 收窄为 G6 的影像 FAIR 部分 | G6 有 0.10 FTE；可参考 [AUG] SPR FAIR app 的做法 |
| #6 遗传学因果层 | 保留并自建，作为靶点档案 Agent 的遗传模块（见 P4b） | 在已有 pQTL/PheWAS（OTv4）基础上扩展，统一进自己的证据 schema |
| D 线成药性 Agent 大量投入 | 控规模，并提醒 FTE 失衡 | G2 只有 0.05 FTE，但 RIC-403/407/392/393/396 活跃度很高；需要和经理对齐，要么加 FTE，要么收敛到 Red line 第 4 条（modality）相关的问题 |

---

## 3. 更新后的项目计划（按与 scope 的对齐度和 ROI 排序）

### P1. Safety Landscape Tool 达到 Highway 全面运行标准（G3 0.15，截止 2026-12-31）

为什么：它是 Red line 第 5 条的门禁（FACT），Highway 1 月起全面运行。

交付物：
- a. 周转 SLA 与容量声明：例如单靶点 X 天、每月 Y 个。这正是 [TH] 要求各部门定义的 "capacity and running process"。
- b. 约 1000 靶点压测（G3 原文），报告失败率和耗时。
- c. 句子级否定修复（RIC-400 / PEX16 类严重漏判）由 deferred 提前。对门禁来说，假 GREEN 是最贵的错误。
- d. 校准与"证据不足"输出（HYP）：门禁需要知道什么时候不能放行。

挂卡：RIC-349（方法）、RIC-404（lifecycle / Portal）。

### P2. 干湿一致性：Red line 安全门槛的外部验证（G3 + G4，约 2 周）

- 做法：对 RIC-381 的 175 个 HepG2 靶点跑安全工具，与 ATP / TMRM 毒性信号比对（混淆矩阵、秩相关、RED 与 Non-RED 的效应量）。
- 价值：给 P1 的门禁提供第一份自有湿实验证据；同时给 G4 Model Characterization 一个明确的落地用途。
- 局限（需写明）：HepG2 体外毒性 ≠ 人体安全性，只能作为一致性信号，不能证明门禁正确。
- 挂卡：新开 Capability 卡，关联 349 + 381。

### P3. 影像管线成为 Highway 标准数据包（G1 0.30 + G5 0.20，截止 2026-12-31）

为什么：SkM atrophy / hypertrophy 是 Muscle preservation 的 primary，SkM FAO / Seahorse 是其 secondary，Adipocyte lipolysis 是 Lipolysis 的 primary（FACT §1b）。每月一轮，要求标准化、不定制，结论二元。

交付物：
- a. 每个 assay 一个固定 SOP，包括：batch 接入 → QC（RIC-342 离群检测前置）→ readout HTML → 数据包模板。复用 myotube BP v2.0 的模式。
- b. 每个 assay 的周转时间与容量声明，对齐每月一轮的节奏。
- b2. 预先定义 hit-call 规则：
  - 以 NTC 为参照的效应量 / SSMD 阈值
  - 方向需与 leading MOA 一致
  - 记录 KDE 字段
  - "repeat 后一致"判定

  输出 POSITIVE / NEGATIVE / INCONCLUSIVE，不留给逐批人工判断。阈值需与 assay owner 共同拍板（SkM：IGWU/YLV；Lipolysis：OFGM/UHYG；SkM FAO：IGWU/YBYI）。
- b3. data package 模板覆盖 Highway 决策树的每个节点：一轮结果 → KDE 核实 → repeat → package。
- c. 确认 #6 Insulin sensitization campaign 的 pAKT 类 assay 是否走影像（HYP，需问 assay owner）。如果是，提前准备。

挂卡：RIC-394（应用日志）、RIC-375、RIC-390、RIC-379（BP）。

### P4. 靶点档案 Agent（自建），首个场景：Red line 预检（G3 + G2，MVP 于 Q1 2027）

- 做法：输入靶点和方向，输出一份带出处的档案，第一版按 Red line 六条组织：
  - 第 3 条：自建表达查询层，直接读 RCCOmics 参考数据集并内置 §1b 的完整阈值表（按细胞、assay、方向区分，例如 SkM siRNA 抑制要求 TPM > 30、激活要求 TPM > 10；in vivo 用 BKNM0140 加 DIO 蛋白组排名 < 8000 且 unique peptides ≥ 2）。阈值表做成配置文件，因为规则仍在 pilot 期调整。
  - 第 5 条：调自己的安全工具
  - 第 6 条：临床抗癌反向、临床安全信号、orphan receptor、胞内激活且无临床工具化合物（ChEMBL / ClinicalTrials 等）
  - 第 1–2 条：in vivo / in vitro 文献证据，做草稿供人审核
  - Highway 进入条件：只允许一个 leading MOA → 推荐对应的 MOA cluster 和 primary/secondary assay，并列出 owner（§1b）；modality 规则（siRNA / protein / 临床阶段小分子）；CVD / MASH 自动提示走 Classic-way。
  - 下游输出：自动起草 in vivo Highway 的 one-pager（适应症、假设 MoA、扰动方式），以及 in vitro positive 靶点之间的证据排序。后者用于争取每季度 7 个的 in vivo slot。
  - 加分模块：成药性（P7）、BBB、virtual-cell 表型（381）、遗传学（P4b）
- 架构：统一证据 schema（claim / 方向 / 来源 / 置信度 / 时间戳），每个模块独立可测（按每模块一个独立单测的规范）；入口复用 RIC-395 Shiny 表单；输出用 HTML 档案，并写入 dashboard。
- 边界：只做预检和证据整理，裁决仍由工作组和 YLV 作出（FACT [OPS] slide 3）。
- 实施顺序：先定 schema，再接入安全和表达两个模块（覆盖 Red line 第 3、5 条，价值最高），然后逐步接入第 6、1–2 条及加分模块。
- 挂卡：新开 Capability 卡。

### P4b. 遗传学因果层（自建，P4 的模块，Q1–Q2 2027）

- 在现有 pQTL / PheWAS（OTv4，cis 定义为 ±1 Mb）基础上，增加：
  - GWAS 共定位（coloc / SuSiE）
  - 孟德尔随机化（cis-MR，以 pQTL/eQTL 为工具变量）
  - rare-variant burden（pLoF）方向一致性检查。参照 [AUG] 中 FNIP1 的用法：用 LoF 方向支持 inhibition 假说。
- 输出：遗传支持的方向（与 Red line 第 4 条的 perturbation hypothesis 对齐），以及证据强度分级。
- 数据：公共 GWAS summary statistics、UKB-PPP / deCODE pQTL、GTEx eQTL，不能访问的通过 Open Targets 获取。下载受 Zscaler 拦截时按已知的替代路径处理。
- 价值：直接对应 "stick to the HYPOTHESIS"，给方向性假说提供人类遗传证据，对 RIC-407 GIGYF1 这类靶点立即有用。

### P5. G4 Model Characterization 收口（G4 0.10）

- RIC-381 状态从 Analysis 转到 In Progress，补 Description，并把四模态 characterization 整理为可交付的 package。
- 只保留一个前沿扩展：held-out 靶点的跨模态预测（DRUG-seq → TMRM/ATP，对比 NTC 置换基线）。这能回答"模型是否有用"，也对接 AIDR 3.2 "AI powered virtual assays into TDE Campaigns"（FACT [AIDR25]）。
- 外部 HepG2 Perturb-seq（Nadig/Replogle，CRISPRi essential genes）的一致性检验列为可选，先算靶点 overlap 再决定。
- 不扩展：主动学习、新的视觉基础模型 A/B，本年度不做。

### P6. 影像数据 FAIR（G6 0.10）

- 以 batch registry 加元数据 schema 起步（plate / well / perturbation / batch / assay / 路径），OME-Zarr 只做试点。
- 参照 [AUG] SPR data FAIR app 的做法（自动取数加设计元数据映射）。
- 遵守 G5 "不做 omics" 的边界，omics fairness 由 IJDN / LZLZ 主导。

### P7. 成药性 Agent：收敛，并与经理对齐 FTE（G2 0.05）

- OBS：活跃度明显超出 0.05 FTE。
- 建议在 1:1 上二选一：
  - (a) 正式加 FTE，改挂 Capability；
  - (b) 收敛到 Red line 第 4 条（modality）和第 6 条中与 modality 相关的排除项（orphan receptor/ligand 不能用 protein/peptide/SM 走 Highway；胞内激活靶点需有临床阶段工具化合物）的快速判断，再加 Highway 蛋白序列选择（每靶点最多 3 条）的结构依据。
- 无论哪种，数值一律标注为相对排序，并补已知配体的校准散点图。

### P8. G8 Training（0.05）

H2 至少完成一次正式会议或课程（FACT [1on1] 标为未完成）。

---

## 4. 看板卫生（沿用 v1 §2，按 Goal 归类）

- 关 Review 积压（146 天）：RIC-244 / 245 / 246 的内容已并入 381 → Done；262、270、331、218 → 一次性过 review；384 → Done（后续见 388/389）。
- 停滞卡：209、217、254、292（467–517 天）走 Closure 或补现状；DBIO-455 确认归属。
- 去重：RIC-392 和 393 合并。
- 每张卡在 Description 里加一行 "Goal: G#"，让月报和 Goal review 可以直接聚合。

## 5. 时间线

| 时间 | 事项 |
|---|---|
| 10 月 | 看板卫生；P2 干湿一致性；P1-c 否定修复启动 |
| 11 月 | P1-a/b SLA 与压测；P3 SOP、hit-call 规则（与 assay owner 共同确定）和数据包模板；P5 中 381 的 Description 与 package |
| 12 月（Highway pilot 收尾） | P1、P3 交付 "capacity and running process" 声明；P5 held-out 预测结果；P8 完成 |
| Q1 2027 | P4 靶点档案 Agent MVP（schema + 安全 + 表达模块）；P6 FAIR 试点 |
| Q1–Q2 2027 | P4b 遗传学因果层；P4 接入第 6、1–2 条及加分模块 |
| 1:1 待议 | P7 的 FTE 选择 |

## 6. 局限与假设

- [OPS] 已逐页读取文字、表格、分组形状和审阅批注；嵌入图片多为图标，未发现图片中有额外规则。其他 PDF 只读了文字层。
- Operational Model 是 2026-07 版本，批注显示序列数、剂量数、CVD/MASH 覆盖仍有争议，需以最新版或 Q&A 文档（NNRCC Operation Model Q&A.docx，未在该目录中找到）为准。
- "pAKT 类 assay 是否走影像"、"Highway 是否要求各 assay 提供 SLA"属于推断，需向 assay owner 或 YLV 确认。
- FTE 是计划值，不代表实际投入；P7 的失衡判断基于 Jira 活跃度，未做工时统计。

---

## 7. 探索性增长点（v2.3 新增）

### 7.0 筛选标准与依据

只保留同时满足以下四条的方向：

1. 影响力：能直接作用于组织 2030 目标中的某个杠杆，即 PoS、turnover 或 innovation source（[OPS] slide 20–21）。
2. 不可替代：建立在我独有的数据或流程位置上，例如 Highway 每月产出的结果流、自有影像数据、我在安全门禁里的角色，而不是重复外部已有的工作。
3. 可证伪：3 个月内能做出 MVP，并且事先写明止损条件。
4. 前沿依据：有 2024–2026 年的同行评审论文或权威发布支撑（FACT，均已检索确认）：
   - 遗传支持使临床成功率提高约 2.6 倍：Minikel et al., Nature 2024，https://www.nature.com/articles/s41586-024-07316-0
   - 深度学习做扰动预测尚未超过简单线性基线：Ahlmann-Eltze et al., Nat Methods 2025，https://www.nature.com/articles/s41592-025-02772-6
   - Systema：指出系统性变异会让扰动预测效果被高估，Nat Biotechnol 2025，https://www.nature.com/articles/s41587-025-02777-8
   - 27 种方法、29 个数据集的扰动预测基准，Nat Methods 2025-12，https://www.nature.com/articles/s41592-025-02980-0
   - Arc Virtual Cell Challenge：2025 年为跨细胞类型泛化；2026 年改为 zero-shot（六个未见过扰动的细胞系，不提供训练集），https://arcinstitute.org/news/virtual-cell-challenge-2026 ；State 模型 https://biorxiv.org/content/10.1101/2025.06.26.661135v2
   - Robin 多智能体全自动科研系统，Nature 2026-05，https://www.nature.com/articles/s41586-026-10652-y ；Biomni 通用生物医学 agent，https://biomni.stanford.edu/
   - Genentech lab-in-the-loop 抗体设计，bioRxiv 2025，https://biorxiv.org/content/10.1101/2025.02.19.639050
   - FNIP1 罕见 LoF 与代谢获益，Nature 2026，doi 10.1038/s41586-026-10864-2（也是 [AUG] 中 FNIP1 立项的依据）
   - UKB-PPP 血浆蛋白组（54,219 人），Nature 2023，https://www.nature.com/articles/s41586-023-06592-6
   - BindCraft one-shot binder 设计，Nature 2025，https://www.nature.com/articles/s41586-025-09429-6
   - GLP-1 减重伴随的肌肉流失，Nat Rev Endocrinol 2025，https://www.nature.com/articles/s41574-025-01160-6
   - JUMP 过表达/敲低形态图谱，Nat Methods 2025，https://nature.com/articles/s41592-025-02753-9 ；Recursion EFAAR 基准，PLoS Comput Biol 2024，https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012463

前沿的共同信号（OBS）：
- 模型本身正在变成标准件，而且很容易被高估（见上面 Nat Methods 和 Systema 两篇）。
- 真正稀缺的是两样东西：一是持续产生的、有对错的前瞻性实验结果（lab-in-the-loop），二是人类遗传给出的方向性证据。
- Highway 恰好让 NNRCC 每月都能产生前一种：6 个 cluster，每个每月一轮，结果为 positive 或 negative。这是我最大的结构性机会。

### 7.1 增长点清单（按影响力 × 不可替代性排序）

#### E1. Highway Oracle：在实验前预测 Highway 结果，并逐月前瞻记分（旗舰）

- 是什么：每轮 Highway 开跑前，对每个靶点和 assay 预测 P(positive)，并给出理由。预测打 hash 存档；出数后自动记分，持续更新模型。也就是 lab-in-the-loop。
- 为什么高影响：
  - 2030 目标要求 PreG 增加约 6 倍。in vitro 是每月一轮，in vivo 每季度只有 7 个 slot，排序准确度直接决定通量和 PoS（[OPS]）。
  - 训练标签由组织运营流程每月自动产生，外部团队拿不到。这是护城河。
- 输入特征：
  - P4 档案（安全、表达阈值余量、遗传方向）
  - 文献 MoA 支持度（LLM 抽取）
  - 381 的 virtual-cell 表型
  - 历史 Highway 和 campaign 结果，可回溯 1144 个已验证靶点的记录（[OPS] notes）
- MVP（3 个月）：
  - 先用历史 campaign 数据（#31/#24/#22、EE campaign、futile cycling）做回溯 AUC
  - 2027 年 1 月起前瞻记分
- 止损：
  - 回溯 AUC 不超过"表达加文献计数"简单基线，即停；
  - 或前瞻 3 轮之后仍不超过基线，即停。
- 依赖：需要 Highway 结果的结构化回收，P3 的 hit-call 规则正好提供这一点。需在 1:1 和 YLV 工作组层面确认数据可用。
- 与现有计划的关系：P3 产出标签，P4 产出特征，E1 是两者合起来的上层，不是另起炉灶。

#### E2. Genetics-first 靶点发现引擎：系统挖掘保护性 LoF（只用免申请的公开数据）

- 是什么：在 cardiometabolic 表型上系统扫描以下证据，输出带方向（抑制 / 激活）的候选清单，送入 Individual target 通道：
  - 罕见 pLoF burden
  - cis-pQTL 共定位 / MR
  - GWAS credible set 与 L2G
  - 并筛出"保护且无明显不良 PheWAS"的靶点
- 为什么高影响：
  - 遗传支持使临床成功率约提高 2.6 倍（Minikel 2024）。
  - FNIP1 就是这条路径的现成成功案例（Nature 2026，[AUG]）。
  - 我是 Individual target 工作组成员（[OPS] slide 3），批注指出这一通道要求"systematic and thorough"覆盖。
- 直接服务 Red line：方向性证据对应第 4 条；不良 PheWAS 补充第 5 条。

数据层：免申请优先（2026-10-14 在 hpccnrd001 实测）

| 优先级 | 数据源 | 内容 | 访问方式 | 实测 |
|---|---|---|---|---|
| 1（主干） | Open Targets Platform 26.09，EBI FTP `ftp.ebi.ac.uk/pub/databases/opentargets/platform/latest/output/` | `evidence_gene_burden`：55,016 条罕见变异 burden 证据，来源包括 AZ PheWAS（UKB 470k）、Regeneron（UKB 450k）、Genebass、Genes & Health、FinnGen，带 `directionOnTarget`/`directionOnTrait`（LoF→protect/risk）；`credible_set`、`colocalisation`、`l2g_prediction`、`study`（含 UKB_PPP_EUR 2,953 个和 Sun_2018 802 个 pQTL 研究、FinnGen R12 2,336 个、GWAS Catalog 163k 个） | 匿名 HTTPS 下载 parquet，无需注册 | 200 OK；已下载 gene_burden 和 study 并解析 |
| 1 | Open Targets GraphQL API | 同上，按靶点实时查询 | 匿名 | 200 OK |
| 2 | GWAS Catalog summary statistics FTP | 完整 GWAS / pQTL 汇总统计，包括 UKB-PPP 的 GCST 镜像，用于自己跑 coloc / MR | 匿名 FTP/HTTPS | 200 OK |
| 2 | Pan-UKBB（AWS Open Data） | 7,221 个 UKB 表型的多祖源 GWAS 汇总统计 | 匿名 S3 / HTTPS | 200 OK |
| 3（核对用） | AZ PheWAS Portal（azphewas.com） | 基因层 collapsing PheWAS 网页查询；bulk 下载目前只有 CNV | 网页匿名 | 200 OK |
| 3 | AZ CGR bulk（public.cgr.astrazeneca.com） | UKB 500k CNV PheWAS 汇总统计 | 匿名，需遵守 LICENSE | 200 OK |

需要登记或付费的数据源，暂不纳入：
- UKB-PPP Synapse 原始数据：需 Synapse 账号（实测 403）。改用 Open Targets 的 UKB_PPP_EUR credible set 和 GWAS Catalog 镜像代替。
- deCODE pQTL：需填写下载表单。
- FinnGen 全量 summary statistics：需填写表单。改用 Open Targets 内的 FinnGen R12 结果代替。
- Genebass 全量 Hail MatrixTable：GCS requester-pays，需要 Google 计费账号。改用 Open Targets 内的 Genebass 子集代替。
- UKB RAP 个体数据：需正式申请。不在 E2 范围内。

可行性抽查（FACT，基于 OT gene_burden 本地解析）：

| 靶点 | 结果 |
|---|---|
| PDE3B | 355 条，TG 方向 LoF→protect，p=2e-60 |
| ANGPTL4 | 97 条，TG 方向 LoF→protect，p=2e-44 |
| PCSK9 | ApoB/LDL 方向 LoF→protect，p≈5e-185 |
| APOC3 | TG 方向 LoF→protect |
| MC4R | 体重方向 LoF→risk |
| GRB14 | FinnGen T2D 方向 LoF→protect，p≈6e-6 |

  - 已知靶点方向全部正确，说明主干数据能支撑方向性筛选。
  - 盲区：FNIP1 只有 2 条（SHBG），没有出现 Nature 2026 报道的代谢获益信号；GPR75 为 0 条；INHBE 只有出生体重一条。
  - 原因（推测）：最新的大样本 exome 结果（Regeneron 约 100 万外显子组、GPR75 研究）尚未进入 OT 的 burden 数据集。
  - 应对：
    - 对重点候选，用论文补充表和 GWAS Catalog 手动补录；
    - 把"文献已报道但 OT 未收录"做成一个显式字段，提醒人工复核，不能当作"没有遗传证据"。

- MVP（4–6 周，纯公开数据）：
  1. 拉取 OT 的 gene_burden、credible_set、colocalisation、l2g、study，本地落 parquet（约几 GB），记录 release 号以便复现。
  2. 表型映射：用 EFO 本体把 T2D、obesity/BMI/体脂分布、MASH/肝脂、TG/ApoB 映射为表型集合。
  3. 打分：
     - burden 的 LoF 方向和效应量
     - cis-pQTL 与 GWAS 共定位（H4 或 colocPIP）
     - L2G
     - 不良 PheWAS 惩罚（risk 方向的严重疾病表型）
     - 输出建议的扰动方向（LoF 有保护作用 → inhibition / siRNA）
  4. 回查：用已知成功或失败靶点（PDE3B、GRB14、ANGPTL4、PCSK9、APOC3 为阳性；sDLK1 等 discontinued 靶点为参考），与 OT `association_by_datatype` 的 genetic 分数做 top-k 召回比较。
  5. 输出 T2D、obesity、MASH 三个表型各 top-50 候选，每个候选带证据链接。
- 止损：如果回查召回率不超过直接按 OT genetic association score 排序，就降级为 P4b 的一个模块，不再单独推进。
- 关系：P4b 是"对给定靶点做评估"，E2 是"主动发现新靶点"，两者共用同一套 OT 数据层。

#### E3. Zero-shot virtual cell 落地 NNRCC 细胞，并设严格基线门槛

- 是什么：用公开的 virtual-cell 模型（State 等，VCC 2026 正好在比 zero-shot），预测 NNRCC 细胞（hepatocyte、adipocyte、SkM）中 siRNA 敲低的转录组和表型效应，用来给 E1 提供特征、给 Highway 做 assay 预筛。
- 为什么值得探索：如果有效，能把"没测过的靶点"变成可排序的；而 VCC 2026 是检验 zero-shot 能力的公开基准。
- 为什么必须设门槛：Nat Methods 2025 和 Systema 指出，深度学习常常跑不赢线性或均值基线。
- 做法：用 381 的 DRUG-seq / TMRM / ATP 做 held-out 评估，必须同时报告线性基线和 Systema 风格的去系统性变异指标。
- 止损：在自有 held-out 上不能稳定超过线性基线，即停，只保留线性模型作为 E1 的特征。
- 资源：GPU 推理即可，不需要湿实验。

#### E4. Muscle preservation 形态图谱：GLP-1 时代的肌肉保留靶点

- 是什么：把每月 Highway 的 SkM atrophy / hypertrophy 影像和历史 IGWU 批次统一做自监督 embedding，建成一个持续积累的"肌肉保留扰动图谱"。用 EFAAR 风格的基准检验它能否召回已知通路（IGF/AKT/mTOR、myostatin/ACVR、FoxO/atrogin），再用它发现新的保护性扰动。
- 为什么高影响：
  - GLP-1 减重伴随的肌肉流失是行业热点（Nat Rev Endocrinol 2025）。
  - Muscle preservation 是 Highway 的六个 cluster 之一。
  - 我拥有这条线的影像管线和历史批次（RIC-261/394）。
- MVP：用现有 IGWU 批次跑 embedding 和召回基准，再与手工特征（SSMD）对比。
- 止损：embedding 召回不超过手工特征，就保留手工特征，只把图谱作为可视化工具。
- 注意：IGWU 两批的 IGF 效应方向矛盾尚待 bench 确认（已知风险），图谱不能跨不同 SSMD 参照直接比较。

#### E5. 自主分析 Agent：从"管线"到"每月自动出 Highway 读数和下一步建议"

- 是什么：参照 Robin（Nature 2026）和 Biomni，把 P3 管线、P4 档案和 E1 打分串起来。数据入库后，Agent 自动完成 QC、hit-call、对照文献与遗传解释，起草 data package 和下一步建议（repeat、secondary assay、in vivo one-pager），交人工审核后发出。
- 为什么：组织要的是 turnover，Highway 要求不做定制，二者都需要不依赖人力逐个处理。
- 止损：人工审核修改率持续超过 50%，就退回半自动模式。
- 定位：它是 E1 和 P3 的交付形态，不单独占 FTE。排在最后，因为它依赖前面几项都成熟。

#### E6（条件性）. Highway 蛋白通道的计算设计序列

- Highway 允许每个靶点最多 3 条蛋白序列，每月第 1 和第 3 个周一提交，8 周交付（[OPS] slide 9）。
- 可以用 BindCraft（Nature 2025）或成药性 Agent 结构流程生成和排序 minibinder 或肽变体，作为这 3 条序列中的候选。
- 限制：Red line 第 6 条排除 orphan receptor/ligand 使用 minibinder 这类 modality；实际执行需要 target champion 同意使用设计序列。
- 只在有 champion 主动邀请时启动，不主动占用 FTE。它也是 P7 成药性线最有可能产生直接影响的出口。

### 7.2 资源与节奏

- 探索预算建议不超过 0.10 FTE（HYP，需在 1:1 确认）。来源可以是 G4 的一部分，或者把 P7 收敛后省下的时间。
- 优先顺序：
  - E1 与 E2 先行，两者都直接利用组织流程，且不需要额外湿实验。
  - E3 和 E4 作为 E1 的特征来源，按止损条件推进。
  - E5、E6 后置。

| 时间 | 探索里程碑 |
|---|---|
| 2026-11 | E1 回溯数据集整理（历史 campaign 和 Highway pilot 结果）；E2 数据层落地（OT 26.09 parquet + GWAS Catalog，全部免申请） |
| 2026-12 | E1 回溯 AUC 对比简单基线（第一个止损点）；E2 三表型 top-50 及已知靶点回查 |
| 2027-01 起 | E1 每月前瞻记分（hash 存档）；E3、E4 在自有 held-out 上对比基线 |
| 2027-Q2 | E1 前瞻满 3 轮后决定继续或停（第二个止损点）；E5 原型 |

### 7.3 风险

- 数据可得性：E1 依赖 Highway 结果的结构化回收和历史 campaign 结果的访问权限；E2 已改为只用免申请的公开数据（见 E2 数据层），代价是最新大样本 exome 结果有滞后，需手动补录。E1 的数据权限仍需确认。
- 过拟合与选择偏差：历史 campaign 的靶点不是随机选的，回溯 AUC 会偏乐观，因此以前瞻记分为准。
- 声誉风险：预测类工具一旦被当成决策依据，错判代价很高。始终定位为排序和提示，裁决仍归工作组和 TC，与 P4 的边界一致。
