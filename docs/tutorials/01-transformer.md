# 01 · Transformer and Language Modeling

## Core question

How can an objective that predicts only the next token become the foundation for general-purpose models?

The key contribution of the Transformer is not “understanding language more intelligently.” It turns sequence modeling into a computation pattern that scales across parallel training: each position reads context through attention, and the same parameters can be applied repeatedly across more data and tasks.

## Minimal form

Given a token sequence $(x_1, \ldots, x_T)$, an autoregressive language model maximizes:

\[
\log p(x_{1:T}) = \sum_{t=1}^{T} \log p(x_t \mid x_{<t})
\]

The core attention computation is:

\[
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

These two equations are enough to define the first implementation target. Do not add RLHF, tool use, or complex distributed training yet. First confirm that the model can overfit a tiny corpus, then observe what structure it extracts from the data.

## Experiment tasks

- Implement a decoder-only Transformer on a small corpus.
- Change model width and depth while keeping data and training steps fixed.
- Record training loss, validation loss, parameter count, throughput, and memory.
- Hold out a compositional task and observe the difference between memorization and generalization.

Experiment directory: [001 · tiny transformer](https://github.com/charliememory/agi-frontier/tree/main/experiments/001-tiny-transformer).

## Failure modes

- Training loss falls while validation loss does not: the model memorized the data.
- Cost rises quickly with context length: the quadratic complexity of attention remains a basic bottleneck.
- Language is fluent but facts are wrong: next-token probability is not the same as truth in the world.

## Current judgment

The Transformer is strong infrastructure for general-purpose prediction, but it does not by itself guarantee grounding, reliable verification, or long-horizon action. The next advances come from expanding the prediction target and closing the feedback loop, not only from lowering the same loss.

## Next step

The next tutorial treats scaling laws as an experimental question: how should parameters, data, and training tokens be allocated under a fixed budget?
