# 01 · Transformer 与语言建模

## 核心问题

为什么一个只预测下一个 token 的目标，能够成为通用模型的基础？

Transformer 的关键贡献不是“更聪明地理解语言”，而是把序列建模变成了适合大规模并行训练的计算结构：每个位置可以通过 attention 读取上下文，再用同一套参数反复应用到更多数据和更多任务。

## 最小形式

给定 token 序列 (x_1, x_2, ldots, x_T)，自回归语言模型最大化：

\[
\log p(x_{1:T}) = \sum_{t=1}^{T} \log p(x_t \mid x_{<t})
\]

注意力层的核心计算是：

\[
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

这两个公式足以作为第一份实现的靶心。先不要加入 RLHF、工具调用或复杂并行训练；先确认模型能过拟合一个极小语料，再观察它如何从数据中获得结构。

## 实验任务

- 用一个小语料实现 decoder-only Transformer。
- 在固定数据、固定训练步数下改变模型宽度和深度。
- 记录训练 loss、验证 loss、参数量、吞吐和显存。
- 留出一个从未出现的组合任务，观察“记住”与“泛化”的差别。

实验目录：[001 · tiny transformer](https://github.com/charliememory/agi-frontier/tree/main/experiments/001-tiny-transformer)。

## 失败模式

- 训练 loss 下降，但验证 loss 不下降：模型只记住了数据。
- 上下文长度增加后成本快速上升：attention 的二次复杂度仍是基础瓶颈。
- 语言流畅但事实错误：下一个 token 的概率并不等于世界中的真值。

## 当前判断

Transformer 是通用预测器的强基础设施，但它本身不保证世界 grounding、可靠验证或长期行动。后续技术的关键，是扩大预测对象和反馈闭环，而不是只把同一个 loss 做得更低。

## 下一步

下一篇将把 scaling law 当成实验问题：在有限预算下，参数、数据和训练 token 应该如何分配？
