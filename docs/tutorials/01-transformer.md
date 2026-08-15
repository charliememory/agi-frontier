# 01 · Transformer and Language Modeling

## Learning objective

By the end of this tutorial, you should be able to:

- derive causal self-attention from the next-token objective;
- trace the shape of every tensor through one decoder block;
- explain why attention made large-scale training easier without claiming that it solved truth,
    grounding, or planning;
- distinguish memorization, in-distribution prediction, and compositional generalization with an
    experiment.

## Core question

How can an objective that predicts only the next token become the foundation for general-purpose models?

The key contribution of the Transformer is not “understanding language more intelligently.” It turns sequence modeling into a computation pattern that scales across parallel training: each position reads context through attention, and the same parameters can be applied repeatedly across more data and tasks.

## Historical bottleneck

Before the Transformer, recurrent models processed sequence positions in order. Their hidden state
created a serial path through time: position $t$ depended on the completed computation at position
$t-1$. Convolutional sequence models improved parallelism but needed multiple layers or dilation to
connect distant positions.

Self-attention shortened the interaction path between any two positions and allowed all training
positions in a sequence to be computed together. This was a scaling breakthrough. It was not, on
its own, a solution to data quality, objective design, evaluation, or environment interaction.

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

## From tokens to logits

For a batch of token IDs with shape $[B,T]$:

| Operation                              | Output shape           | Purpose                                                  |
| -------------------------------------- | ---------------------- | -------------------------------------------------------- |
| Token embedding + position information | $[B,T,d]$              | Represent symbol identity and order                      |
| Linear projections to $Q,K,V$          | $[B,T,h,d_h]$          | Create queries, keys, and values per head                |
| Attention scores $QK^T/\sqrt{d_h}$     | $[B,h,T,T]$            | Compare every query position with every key position     |
| Causal mask + softmax                  | $[B,h,T,T]$            | Prevent reading future tokens; normalize context weights |
| Weighted values                        | $[B,T,d]$              | Aggregate context-dependent information                  |
| MLP and residual updates               | $[B,T,d]$              | Transform each position while preserving an update path  |
| Vocabulary projection                  | $[B,T,\lvert V\rvert]$ | Produce next-token logits                                |

Multi-head attention does not merely repeat one attention map. Each learned projection can organize
information differently, although interpreting a head as one stable human-readable function is
usually unsafe.

## Causality and training parallelism

During training, the model predicts every next token in the sequence in one operation. The causal
mask prevents target leakage even though the hardware computes positions in parallel. During
generation, outputs remain sequential because token $t+1$ is not known until token $t$ has been
sampled or selected.

This distinction explains two important facts:

- Transformer **training** parallelizes over sequence positions.
- Autoregressive **generation** still has a serial dependency, motivating KV caching, speculative
    decoding, parallel decoding proposals, and alternative generation objectives.

## What the objective can learn

Next-token prediction is dense supervision: every token supplies a target, and predicting text well
requires capturing many regularities that generated it. Syntax, style, factual associations, code
patterns, and some task procedures can therefore emerge from the same objective.

But the loss rewards probability assigned to observed continuations, not truth or successful action
directly. A model can lower loss by exploiting correlations that fail under distribution shift. It
can also represent knowledge without reliably retrieving or applying it in a particular prompt.

Keep three claims separate:

- **Fact:** autoregressive models minimize predictive loss over sequences.
- **Interpretation:** sufficiently broad prediction encourages reusable internal representations.
- **Open hypothesis:** prediction plus scale is sufficient for all capabilities needed by AGI.

The tutorial tests the first two; it does not assume the third.

## Controlled comparison

Use a synthetic language alongside a tiny natural-language corpus. Generate sequences from simple
rules such as:

```text
alice likes red square
bob likes blue circle
query alice red → yes
query alice blue → no
```

Create three evaluation sets:

1. **Seen combinations:** examples present in training.
1. **New samples, familiar combinations:** different sequences from the same distribution.
1. **Held-out compositions:** familiar primitives combined in ways never shown during training.

Run at least two model sizes with the same training examples and optimization budget. Record exact
match or token accuracy for each split. A larger memorization gap is not evidence of stronger
generalization.

## Diagnostics before interpretation

- Overfit one batch. Failure usually indicates an implementation or optimization problem.
- Compare against a unigram or n-gram baseline. The Transformer should earn its complexity.
- Inspect the causal mask by changing a future token and confirming that earlier logits do not
    change.
- Shuffle labels. A model that performs above chance may be seeing leakage.
- Repeat with multiple seeds before interpreting a small difference.
- Report parameter count, tokens processed, wall-clock time, and peak memory with accuracy.

## Experiment tasks

- Implement a decoder-only Transformer on a small corpus.
- Change model width and depth while keeping data and training steps fixed.
- Record training loss, validation loss, parameter count, throughput, and memory.
- Hold out a compositional task and observe the difference between memorization and generalization.
- Test causal-mask leakage and compare against a simple non-neural baseline.
- Save at least three failed held-out examples, not only aggregate loss.

Experiment directory: [001 · tiny transformer](https://github.com/charliememory/agi-frontier/tree/main/experiments/001-tiny-transformer).

## Failure modes

- Training loss falls while validation loss does not: the model memorized the data.
- Cost rises quickly with context length: the quadratic complexity of attention remains a basic bottleneck.
- Language is fluent but facts are wrong: next-token probability is not the same as truth in the world.
- Held-out primitives work but held-out combinations fail: component knowledge did not become
    systematic composition.
- A benchmark improves after adding prompt examples: this may be adaptation through context, not a
    change in model parameters or durable learning.

## Anchor sources

Read in this order, with a question for each source:

1. Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — which serial
    bottleneck is removed, and which costs remain?
1. Elman, [Finding Structure in Time](https://doi.org/10.1207/s15516709cog1402_1) — what could
    recurrent next-step prediction already learn before Transformers?
1. Brown et al., [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — what
    changes with scale, and how is in-context learning evaluated?
1. Hoffmann et al., [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)
    — why is architecture alone insufficient to explain capability growth?

The first paper is the mechanism anchor. The others connect that mechanism to its predecessors and
to the next tutorial on scaling.

## Current judgment

The Transformer is strong infrastructure for general-purpose prediction, but it does not by itself guarantee grounding, reliable verification, or long-horizon action. The next advances come from expanding the prediction target and closing the feedback loop, not only from lowering the same loss.

## Next step

The next tutorial treats scaling laws as an experimental question: how should parameters, data, and training tokens be allocated under a fixed budget?

Before moving on, add one ledger entry answering:

> After running the controlled split, how much of the model's apparent competence was memorization,
> distribution-matched prediction, or genuine composition? What evidence would distinguish them
> more sharply?

## Completion checklist

- [ ] I can derive attention and trace the tensor shapes without looking at framework code.
- [ ] I verified that the causal mask prevents future-token leakage.
- [ ] I overfit a tiny batch and compared at least two controlled settings.
- [ ] I reported seen, in-distribution, and held-out-composition results separately.
- [ ] I saved concrete failures and updated my research ledger.
