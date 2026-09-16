---
marp: true
theme: default
paginate: true
size: 16:9
header: '昌平实验室人类基因组25周年研讨会 · AI与靶点安全'
footer: '诺和诺德 R&ED · 数据科学与计算生物学团队'
style: |
  section { font-family: 'Noto Sans CJK SC', 'Noto Sans SC', sans-serif; font-size: 20px; padding: 36px 56px; }
  section.title { text-align: center; justify-content: center; }
  section.title h1 { font-size: 38px; color: #003a70; margin-bottom: 10px; }
  section.title h2 { font-size: 22px; color: #00518a; border-bottom: none; font-weight: normal; }
  h1 { font-size: 28px; margin-bottom: 8px; color: #003a70; }
  h2 { font-size: 23px; color: #003a70; border-bottom: 2px solid #003a70; padding-bottom: 4px; margin-bottom: 12px; }
  h3 { font-size: 19px; color: #00518a; margin: 8px 0 4px 0; }
  table { font-size: 14.5px; border-collapse: collapse; margin: 8px 0; width: 100%; }
  th { background: #003a70; color: #fff; padding: 5px 8px; font-weight: 600; text-align: left; }
  td { padding: 4px 8px; border: 1px solid #d0d7de; }
  blockquote { font-size: 16px; color: #444; border-left: 4px solid #003a70; padding-left: 12px; margin: 8px 0; background: #f6f8fa; }
  code { background: #f0f3f6; padding: 2px 5px; border-radius: 3px; font-size: 15px; }
  ul, ol { margin: 4px 0; padding-left: 24px; }
  li { margin: 3px 0; line-height: 1.35; }
  .small table { font-size: 13px; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px 16px; }
  .card h3 { margin-top: 0; color: #003a70; }
  .bold { font-weight: 600; color: #003a70; }
---

<!-- _class: title -->

# AI基础模型与靶点安全分析
## 昌平实验室“人类基因组25周年”国际研讨会核心精炼

**北京** · 2026年8月24–25日  
**核心聚焦**：调控基础模型、统计约束AI智能体与靶点安全去风险化  
**汇报团队**：数据科学与计算生物学团队

---

## 1. 核心跃迁：从“读懂序列”到“因果预测”

基因组学正从单纯的测序与统计关联，迈进**AI驱动的因果干预时代**：

<div class="grid">
<div class="card">
<h3>过去：观测与相关性分析</h3>
<ul>
<li><b>HGP (2001)</b>：提供静态一维参考坐标系。</li>
<li><b>GWAS / 队列</b>：仅给出P值统计关联，机制仍是黑箱。</li>
<li><b>安全评估 (TSL)</b>：被动检索文献、静态基因约束分（pLI/LOEUF）。</li>
</ul>
</div>
<div class="card">
<h3>现在：预测与机制性AI</h3>
<ul>
<li><b>单分子动力学</b>：直接测定天然DNA上的绝对结合亲和力。</li>
<li><b>调控基础模型</b>：计算预测全基因组TF亲和力改变（Δ<i>K</i><sub>d</sub>）。</li>
<li><b>安全评估 (TSL)</b>：由统计检验严格闭环的多智能体因果推理。</li>
</ul>
</div>
</div>

> **核心目标**：推动靶点安全性评估（TSL）从**被动文献查表**转向**主动机制因果预测**。

---

## 2. 调控基础模型：破译非编码区的脱靶毒性

- **生物学现实**：90%以上的GWAS关联及药物安全性突变位于非编码区，核心机制是改变转录因子（TF）的结合。传统管线缺乏生化解释力，常将其当作黑箱忽略。
- **AI解决方案（谢晓亮 / 陈明辰团队 · `ivtFOODIE` + `Seq2Kd`）**：
  - 基于脱氨酶单分子技术，高通量直接测定天然DNA上的TF绝对结合亲和力。
  - 构建深度学习基础模型 `Seq2Kd`，成功泛化预测约500个缺乏注释的转录因子结合亲和力变化（Δ<i>K</i><sub>d</sub>）。
- **对靶点安全的直接价值**：
  - **预测调控脱靶级联**：提前预测扰动靶点是否会剥离必需转录因子，导致关键下游基因网络塌陷。
  - **解析非编码安全变异**：将原本模糊的非编码eQTL转化为定量的生物物理亲和力破坏分值。

---

## 3. 统计闭环的AI智能体：终结幻觉与假警报

- **生物学现实**：大语言模型（LLM）擅长编造表面合理的生物学假说，在靶点安全评估中容易生成大量无法验证的虚假毒性报警，干扰研发决策。
- **AI解决方案（林希虹院士团队 · `Fever GPT` 架构）**：
  - 汇总全基因组30亿位点、90亿SNV功能注释的超大规模知识图谱。
  - 采用多智能体协作架构，并**硬性嵌入统计学假设检验门禁**（Statistical Gating）。
- **对靶点安全的直接价值**：
  - **因果证据自动交叉验证**：智能体提取的每一条文献安全警示，都必须通过底层人类遗传学（cis-pQTL、PheWAS、罕见变异约束）的统计检验。
  - **零幻觉安全档案**：严格剔除由连锁不平衡或文献偏倚带来的伪毒性关联。

---

## 4. 体细胞演化动力学：重新区分适应与致癌

- **生物学现实**：临床前在靶器官中检测到克隆生长或体细胞突变，传统评估常一律判定为致癌红线（Stop Flag），导致许多有效靶点被错杀。
- **AI与演化图谱方案（Peter Campbell教授 · Quotient / 原Sanger）**：
  - 正常衰老组织每年每细胞积累30–40个突变，70岁以上健康人群普遍存在克隆性造血。
  - **关键发现**：慢性压力诱导的趋同突变（如脂肪肝中的 *FOXO1*, *GPAM*）能保护组织功能，但在**肝癌中受到强烈负选择**。
- **对靶点安全的直接价值**：
  - **体细胞适应度建模**：通过人类演化适应度图谱，精准识别细胞增殖是“良性代偿修复”还是“恶性转化倾向”。
  - **为慢性病靶点去风险化**：为代谢/衰老领域的慢性长周期用药靶点提供客观的致癌风险分层。

---

## 5. 下一代靶点安全评估（TSL）升级矩阵

<div class="small">

| 评估层级 | 当前工业界基准 | AI升级方案 (Post-CPL 2026) | 研发决策价值 |
| :--- | :--- | :--- | :--- |
| **非编码区突变** | 仅依赖编码区约束（pLI, LOEUF） | 转录因子定量结合动力学（`Seq2Kd`） | 精确定位非编码突变是否破坏下游必需基因调控。 |
| **文献与靶点推理** | 人工检索 / 单提示词LLM总结 | 嵌入统计假设检验闸门的多智能体管线 | 终结毒性幻觉，产出具备统计可信度的安全证据链。 |
| **致癌与克隆风险** | 见克隆扩增即亮红灯（强保守策略） | 体细胞适应度与肿瘤负选择突变矩阵 | 避免错杀具备代偿性组织修复功能的慢性病优质靶点。 |
| **表型到机制** | 单一终点读数（如常规毒理筛查） | 序列语法到细胞表型的统一状态表征 | 将高内涵显微成像（HCS）表型变化直接溯源至调控网络重构。 |

</div>

---

## 6. 数据科学团队核心行动原则

<div class="card">
<h3>靶点安全三项核心原则</h3>
<ul>
<li><b>1. 生物物理动力学优于纯P值</b>：引入调控基础模型（预测 Δ<i>K</i><sub>d</sub>），穿透非编码变异的生化机制。</li>
<li><b>2. 严格统计证伪优于表面合理性</b>：为Safety Agent建立自动化遗传学统计校验门禁，坚决过滤虚假安全警告。</li>
<li><b>3. 演化生物学常识优于过度保守</b>：借助体细胞适应度图谱，科学解耦“组织代偿修复”与“肿瘤恶性转化”。</li>
</ul>
</div>

> **总结**：下一代靶点安全的核心，是把传统的**定性疑虑**转化为**有统计约束、有生物物理机理的量化AI预测**。
