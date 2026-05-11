# Email Draft — LLM Hosting Feasibility

> Ready to copy-paste. Replace `[Boss]` and `[Your name]` before sending.

---

**Subject:** Feasibility — Self-hosting DeepSeek-V4-Flash vs. Qwen3.5 on our GPU node

Hi [Boss],

Quick summary of the hosting feasibility study you asked for.

**TL;DR:** DeepSeek-V4-Flash is API-only and cannot be self-hosted. **Qwen3.5-32B** is already deployed and running on our existing vLLM stack — no new hardware needed.

**1. Hardware baseline**
8 × A100-SXM4-40GB (320 GB VRAM, Ampere — no native FP8), 2 × EPYC 7H12, 2 TiB RAM, CUDA 13.0, vLLM Docker already in place. Storage: `/home` ~40 GB free, `/data` ~654 GB free.

**2. DeepSeek-V4-Flash — not self-hostable**
Per DeepSeek's official docs, V4-Pro/Flash are hosted-API only (OpenAI/Anthropic-compatible). No open weights have been released (last open release was V3.1, Aug 2025). Even if weights appeared, a V3-scale 671B MoE (~670 GB FP8) would not fit in 320 GB VRAM, and Ampere can't consume FP8 natively. **Only path today: hosted API.**

**3. Qwen3.5 — fits comfortably**
- **Qwen3.5-32B (already deployed ✅).** Dense 32B, BF16 ~64 GB, runs on TP=2/4 with plenty of headroom. Already serving via our existing vLLM Docker stack.
- **Qwen3.5-35B-A3B** — MoE (35B total / 3B active), vision-capable, 262K native context extensible to ~1M. Worth considering for long-context or multimodal workloads.
- **Qwen3.5-122B-A10B** — AWQ/GPTQ-Int4 comfortable. Good fallback if we need more capacity later.
- Smaller dense variants (0.8B–27B) all fit easily.

Operational notes for Ampere: stick to BF16 or AWQ/GPTQ-Int4 (no FP8 checkpoints); point `HF_HOME` to `/das` before pulling large weights.

**4. Recommendation**
- **DeepSeek-V4-Flash:** consume via hosted API only.
- **Local deployment:** keep **Qwen3.5-32B** as the default (already up and running). Hold **Qwen3.5-35B-A3B** as a long-context/multimodal upgrade and **Qwen3.5-122B-A10B (INT4)** as a larger-capacity fallback.

Happy to dig deeper into any of these.

Best,
[Your name]
