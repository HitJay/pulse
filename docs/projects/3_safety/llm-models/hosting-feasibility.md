# DeepSeek-V4-Flash / Qwen3.5 自托管可行性简报

**日期**：2026-05-11  
**结论**：V4-Flash 必走 API；本地已有 Qwen3.5-32B 跑通可立即使用，推荐升级到 35B-A3B 拿 MoE 效率 + 长上下文 + 视觉，无需新硬件。

---

## 1. DeepSeek-V4-Flash — 无法自托管

- 仅 API 服务，无开源权重（最后开源版本为 V3.1，2025-08）。
- 1M 上下文，定价 ¥0.02 / ¥1 / ¥2 per M tokens（缓存/输入/输出）。
- 即使日后开源，V3 级别 671B MoE FP8 ~670 GB 远超我们 320 GB VRAM，且 A100 无原生 FP8。
- **结论：继续走官方 API。**

## 2. 硬件基线

| 资源 | 规格 |
|------|------|
| GPU | 8 × A100-SXM4-40GB（320 GB VRAM，Ampere，无原生 FP8） |
| CPU | 2 × AMD EPYC 7H12（256 线程） |
| RAM | 2.0 TiB |
| 驱动 | 580.65.06 / CUDA 13.0 |
| 存储 | `/home` ~40 GB · `/data` ~654 GB |
| 推理栈 | vLLM OpenAI-compatible Docker |

## 3. Qwen3.5 选型

| 选项 | 显存 (BF16) | 状态 |
|------|-------------|------|
| ≤27B Dense | ≤56 GB | 可跑 |
| **32B Dense** | ~64 GB | **✅ 已部署成功** |
| **35B-A3B (MoE, 3B active)** | ~74 GB | **推荐升级默认**（262K 上下文、视觉） |
| 122B-A10B INT4 | ~80 GB | 后续备选 |
| 397B-A17B | ~810 GB | 不可行 |

**Ampere 注意**：限定 BF16 / AWQ / GPTQ-INT4，避开 FP8 checkpoint。  
**存储注意**：大模型下载前将 `HF_HOME` 指向 `/das`。

### 35B-A3B 部署命令参考

```bash
vllm serve Qwen/Qwen3.5-35B-A3B \
  --tensor-parallel-size 8 \
  --max-model-len 262144 \
  --reasoning-parser qwen3
```

## 4. 一句话总结

V4-Flash 走 API；本地 32B Dense 已跑通可用，下一步升级 35B-A3B（MoE + 长上下文 + 视觉），无需新硬件。
