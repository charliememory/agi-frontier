# 001 · Tiny Transformer

Status: `planned`

Goal: implement a minimal decoder-only Transformer from scratch and test next-token prediction, overfitting, and basic generalization differences.

Related tutorial: [01 · Transformer and Language Modeling](../../docs/tutorials/01-transformer.md)

## Research question

When a decoder-only Transformer achieves low loss, how much of the result is memorization,
in-distribution prediction, or generalization to a held-out composition?

## Planned comparison

Use both a tiny text corpus and a generated rule-based language. The synthetic data must expose
three distinct evaluation splits:

| Split | What it tests |
| --- | --- |
| `train_seen` | Capacity to memorize or fit observed examples |
| `iid_test` | Prediction on new samples from familiar combinations |
| `composition_test` | Transfer to familiar primitives in held-out combinations |

Run a non-neural baseline and at least two Transformer capacities under a matched data and update
budget. Repeat any close result across at least three seeds.

## Required diagnostics

- Confirm earlier logits do not change when a future token is changed.
- Overfit a single batch before running the main comparison.
- Run once with shuffled targets to detect leakage.
- Record parameters, tokens processed, step count, wall time, and peak memory.
- Preserve at least three failure examples from `composition_test`.

## Files to add

```text
experiments/001-tiny-transformer/
  README.md
  config.yaml
  train.py
  model.py
  data.py
  tests/
  results.md
```

## Acceptance criteria

- [ ] A tiny corpus can be overfit.
- [ ] Validation loss and training loss are logged separately.
- [ ] Run at least one width or depth comparison.
- [ ] Record one failure case and the next question.
- [ ] Causal-mask leakage and shuffled-label controls pass.
- [ ] Seen, IID, and held-out-composition metrics are reported separately.
- [ ] A non-neural baseline and compute accounting are included.

## Result template

Create `results.md` only after the first run:

```markdown
# Results

## Hypothesis
## Setup and compute budget
## Results by evaluation split
## Three concrete failures
## Fact / interpretation / hypothesis
## What changed in the research ledger
## Next falsifiable experiment
```
