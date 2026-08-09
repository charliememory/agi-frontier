# 技术时间线

时间线回答“发生了什么”，能力地图回答“为什么重要”。两者交叉使用，避免把技术史写成名词串。

## 五次预测对象扩张

```text
token → multimodal latent → future trajectory → action → improvement loop
```

| 阶段      | 代表性转折                                      | 新增能力                     | 尚未解决的瓶颈               |
| --------- | ----------------------------------------------- | ---------------------------- | ---------------------------- |
| 2017–2020 | Transformer、预训练语言模型                     | 可扩展的序列表示与生成       | grounding、事实可靠性        |
| 2020–2022 | scaling、instruction tuning、RLHF               | 更好的任务遵循与泛化         | 长时程推理、可验证性         |
| 2021–2023 | CLIP、BLIP-2、LLaVA 等                          | 视觉—语言对齐                | 空间关系、幻觉、长视频       |
| 2020–2024 | diffusion、latent diffusion、DiT、flow matching | 高质量连续分布生成           | 可控性、时序与物理一致性     |
| 2022–2026 | agent、world model、VLA、推理时计算             | 工具使用、预测环境、执行动作 | 在线学习、长期记忆、安全     |
| 现在      | verifier、合成数据、自动实验搜索                | 从一次性训练走向闭环改进     | reward hacking、真实进步判定 |

> 这些支线不是简单的前后继承关系。视觉表示、生成建模和控制学习长期并行，最终在 world model、agent 和 embodied system 中汇合。
