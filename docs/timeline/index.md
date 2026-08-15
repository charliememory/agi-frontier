# Technology Path

A short history of what the field expanded the prediction target to, and which bottleneck each
expansion left open. The [tutorials](../tutorials/index.md) turn the same sequence into learning
units; this page is only the overview.

```text
token → multimodal latent → future trajectory → action → improvement loop
```

| Period    | Representative shift                                   | New capability                                            | Unresolved bottleneck                              |
| --------- | ------------------------------------------------------ | --------------------------------------------------------- | -------------------------------------------------- |
| 2017–2020 | Transformer, pretrained language models                | Scalable sequence representation and generation           | grounding, factual reliability                     |
| 2020–2022 | scaling, instruction tuning, RLHF                      | Better instruction following and generalization           | long-horizon reasoning, verifiability              |
| 2021–2023 | CLIP, BLIP-2, LLaVA, and related work                  | Vision–language alignment                                 | spatial relations, hallucination, long video       |
| 2020–2024 | diffusion, latent diffusion, DiT, flow matching        | High-quality continuous-distribution generation           | controllability, temporal and physical consistency |
| 2022–2026 | agents, world models, VLAs, test-time compute          | Tool use, environment prediction, action execution        | online learning, long-term memory, safety          |
| Now       | verifiers, synthetic data, automated experiment search | A shift from one-shot training to closed-loop improvement | reward hacking, proving real progress              |

These branches are not a simple chain of inheritance. Visual representation, generative modeling,
and control learning evolved in parallel before converging in world models, agents, and embodied
systems.

## When reading a new method

1. **Prediction target** — tokens, patches, latents, frames, future states, actions, or experiment outcomes?
1. **Conditioning state** — text, image, video, trajectory history, tool output, or an environment?
1. **Feedback source** — next-token loss, preference, a verifier, a simulator, or the real world?
1. **Where improvement happens** — parameters, data, prompts, test-time search, or external tools?
1. **Evidence** — reported in a paper, reproduced with public code, independently reproduced, or observed in use?
