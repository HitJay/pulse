# 本地部署候选模型深度调研

**日期**：2026-05-11  
**基准**：Qwen3.5-32B 已在 8×A100-40GB 节点部署成功，本文档调研同硬件下其他值得部署的开源模型。

---

## 1. 硬件约束速查

| 资源 | 规格 | 关键限制 |
|------|------|----------|
| GPU | 8 × A100-SXM4-40GB（320 GB VRAM） | Ampere，**无原生 FP8** |
| CPU | 2 × AMD EPYC 7H12（256 线程） | — |
| RAM | 2.0 TiB | 可支持 CPU offload |
| 存储 | `/home` ~40 GB · `/data` ~654 GB | 下载前须 `export HF_HOME=/das/…` |
| 推理栈 | vLLM OpenAI-compatible Docker | 已稳定运行 |

**量化策略**：仅使用 BF16 / AWQ-INT4 / GPTQ-INT4。避开 FP8-only checkpoint（A100 需 Marlin 反量化，吞吐显著下降）。

---

## 2. 筛选标准

1. **装得下**：BF16 或 INT4 量化后权重 + KV cache 可放入 320 GB VRAM
2. **跑得动**：vLLM 已原生支持该架构（参考 2026-05 vLLM 模型注册表）
3. **用得上**：与 Qwen3.5-32B 在用途上有差异化（更大通用 / 推理 / 编码 / 多模态 / 长上下文）
4. **不是 FP8-only**：排除仅提供 FP8 checkpoint、无 BF16/INT4 变体的模型

---

## 3. 候选矩阵

### 3.1 通用 — 更大容量

| 模型 | 参数量 | BF16 显存 | INT4 显存 | TP 配置 | 亮点 |
|------|--------|-----------|-----------|---------|------|
| **Llama-3.3-70B-Instruct** | 70B dense | ~140 GB | ~40 GB | TP=8 (BF16) / TP=4 (INT4) | 英文最强开源 dense，function calling 成熟，非 Qwen 系避免单一供应商 |

**vLLM 启动命令**：

```bash
vllm serve meta-llama/Llama-3.3-70B-Instruct-AWQ \
  --tensor-parallel-size 4 \
  --max-model-len 131072 \
  --tool-call-parser llama3_json \
  --enable-auto-tool-choice
```

**vs Qwen3.5-32B**：英文 & agentic / tool-use 场景更强；中文略弱；70B 在推理质量上有明显优势。适合作为"大号通用"端点并存。

---

### 3.2 MoE 高效 — 高天花板低推理成本

| 模型 | 总参数 / 活跃 | BF16 显存 | INT4 显存 | TP 配置 | 亮点 |
|------|---------------|-----------|-----------|---------|------|
| **GLM-4.6-Air** | ~106B / 12B active | ~210 GB | ~55 GB | TP=8 (BF16 紧) / TP=4 (INT4) | 清华智谱最新旗舰 MoE，vLLM 支持 MTP 推测解码，中英双语均强 |

**vLLM 启动命令**：

```bash
vllm serve THUDM/GLM-4.6-Air-AWQ \
  --tensor-parallel-size 4 \
  --max-model-len 131072
```

**vs Qwen3.5-32B**：MoE 架构意味着 12B active 推理速度接近小模型，但总知识容量远超 32B dense。建议与 Qwen3.5-32B 做 head-to-head 实测后再决定是否替换为默认。

---

### 3.3 推理 / 数学 / Agents

| 模型 | 参数量 | BF16 显存 | 亮点 |
|------|--------|-----------|------|
| **DeepSeek-R1-Distill-Qwen-32B** | 32B dense | ~64 GB | 长链推理（CoT）最佳同尺寸模型，与 Qwen3.5-32B 同 footprint 可热切换 |

**vLLM 启动命令**：

```bash
vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \
  --tensor-parallel-size 4 \
  --max-model-len 32768 \
  --reasoning-parser deepseek_r1
```

**vs Qwen3.5-32B**：纯推理 / 数学 / 逻辑场景明显更强；通用对话和指令跟随略弱。适合作为"推理专用"端点。

---

### 3.4 编码专用

| 模型 | 总参数 / 活跃 | BF16 显存 | 亮点 |
|------|---------------|-----------|------|
| **Qwen3-Coder-30B-A3B** | 30B / 3B active | ~60 GB | MoE 编码专家，开源编码排行榜领先，推理速度极快（3B active） |

**vLLM 启动命令**：

```bash
vllm serve Qwen/Qwen3-Coder-30B-A3B-Instruct \
  --tensor-parallel-size 4 \
  --max-model-len 131072
```

**vs Qwen3.5-32B**：代码生成、补全、review 等场景专精；通用问答不如 32B。适合与 IDE / Copilot 类前端对接。

---

### 3.5 多模态 / 视觉

| 模型 | 参数量 | BF16 显存 | INT4 显存 | 亮点 |
|------|--------|-----------|-----------|------|
| **Qwen3-VL-32B** | 32B | ~64 GB | ~20 GB | 沿用 Qwen 生态，图片/视频理解 |
| **Qwen3-VL-72B (AWQ)** | 72B | ~144 GB | ~40 GB | 更强视觉理解 |

**vLLM 启动命令**（32B 为例）：

```bash
vllm serve Qwen/Qwen3-VL-32B-Instruct \
  --tensor-parallel-size 4 \
  --max-model-len 32768
```

**vs Qwen3.5-32B**：Qwen3.5-32B 是纯文本模型，如需图片/PPT 截图理解能力则必须换用 VL 系列。

---

### 3.6 长上下文

| 模型 | 总参数 / 活跃 | 上下文 | 显存 | 亮点 |
|------|---------------|--------|------|------|
| **Qwen3.5-35B-A3B** | 35B / 3B active | 262K → ~1M | ~74 GB BF16 / ~20 GB INT4 | MoE + 视觉 + 超长上下文 |
| **Kimi-Linear** | — | 超长上下文 | — | 线性注意力，vLLM 已支持 |

已在 [可行性简报](hosting-feasibility.md) 中详细分析，此处不再展开。

---

## 4. 不推荐在本节点部署的模型

| 模型 | 原因 |
|------|------|
| Llama-4 Maverick | MoE ~400B+，BF16 远超 320 GB；INT4 勉强但 KV cache 不足 |
| Mistral-Large-3 | ~123B dense，BF16 ~246 GB TP=8 紧，且长上下文 KV cache 受限 |
| MiniMax-M2（全精度） | 参数量过大，BF16 不可行 |
| DeepSeek-V3 / V3.1 / V4 | V3/V3.1 671B FP8 ~670 GB 远超 VRAM；V4 无开源权重 |
| 所有 FP8-only checkpoint | A100 无原生 FP8，需 Marlin 反量化，吞吐损失 20-40% |

---

## 5. 推荐部署方案

### 方案 A：三端点阵容（推荐）

```
端点 1 — 通用默认    → Qwen3.5-32B（已部署 ✅）
端点 2 — 编码专用    → Qwen3-Coder-30B-A3B
端点 3 — 推理专用    → DeepSeek-R1-Distill-Qwen-32B
```

三个模型均为 ~60-64 GB BF16，可按需切换（非同时）；或 INT4 量化后多模型并行。

### 方案 B：通用 + 大模型

```
端点 1 — 通用默认    → Qwen3.5-32B（已部署 ✅）
端点 2 — 大号通用    → Llama-3.3-70B-Instruct-AWQ（TP=4，~40 GB）
```

两个端点可**同时运行**（总共 ~104 GB，远低于 320 GB），提供不同容量级别。

### 方案 C：MoE 替代默认

先 head-to-head 实测 **GLM-4.6-Air (INT4)** vs Qwen3.5-32B，若 GLM 在我们实际负载上更优，则替换默认端点。

---

## 6. 下一步

1. [ ] 决定优先部署方案 A / B / C
2. [ ] 下载候选模型权重至 `/das`（注意 `HF_HOME` 指向）
3. [ ] 在实际业务 prompt 上跑 A/B 对比
4. [ ] 更新 vLLM Docker Compose 配置支持多端点

---

## 7. 参考资料

- [vLLM 官方模型注册表（2026-05）](https://docs.vllm.ai/en/latest/)：确认所有候选模型均已原生支持
- [Qwen 官方 HuggingFace](https://huggingface.co/Qwen)
- [GLM 官方 HuggingFace](https://huggingface.co/THUDM)
- [Meta Llama](https://huggingface.co/meta-llama)
- [DeepSeek](https://huggingface.co/deepseek-ai)
- 本节点硬件基线：见 [自托管可行性简报](hosting-feasibility.md)
