# Tutorial Series

This series learns through implementation and failure cases. Each entry does more than summarize papers: it places one mechanism back into a shared AGI framework.

Start with [00 · Orientation](00-overview.md), then use the
[complete roadmap](roadmap.md) to see how language models, multimodal models, generative world
models, VLAs, and self-improving systems converge. The roadmap is dependency-aware; model release
news is tracked separately in the Frontier Radar.

Use the [External Resource Library](../resources/index.md) to triangulate each topic against
established courses, implementation series, and research talks before extending the local syllabus.

## Fixed structure

1. Core question: what was missing from the previous generation?
1. Minimal mechanism: run the critical path with as little code as possible.
1. Controlled comparison: change one variable at a time.
1. Failure case: why did the model fail?
1. Current judgment: what does the evidence support?
1. Next step: one small, testable question.

## Routes

- **Foundations**: Transformer, language modeling, scaling, test-time compute, and post-training.
- **Perception**: vision–language alignment, multimodal tokens, and long-video understanding.
- **Generation**: VAE, diffusion, DiT, flow matching, and video world models.
- **Action**: agents, VLAs, world models, and long-horizon control.
- **Closed loop**: verifiers, automatic task generation, synthetic data, and self-improving systems.

## Current learning sprint

1. Write the first belief baseline in the research ledger.
2. Complete [01 · Transformer and Language Modeling](01-transformer.md).
3. Run [Experiment 001](https://github.com/charliememory/agi-frontier/tree/main/experiments/001-tiny-transformer)
   and record where memorization is mistaken for generalization.
