# Five Tracking Axes

Every tutorial, paper card, and experiment result should answer these five questions where possible.

| Axis                 | Question                                                   | Typical evidence                                                 |
| -------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------- |
| Generalization       | Can it handle new tasks outside the training distribution? | held-out tasks, cross-domain tests, compositional generalization |
| Long horizon         | Can it complete tasks over dozens of steps or more?        | task completion, recovery from errors, trajectory length         |
| Grounding            | Does it model space, time, physics, and causality?         | grounding tests, video prediction, interactive environments      |
| Autonomous learning  | Can it improve from failures and environment feedback?     | online learning, synthetic data, curriculum learning             |
| Reliability and cost | Can results be verified and run at a reasonable cost?      | verifiers, consistency, latency, memory, price                   |

## Avoid a single-benchmark story

Benchmark scores are evidence, not a definition. A system can improve on static knowledge questions without gaining better long-horizon planning. It can also raise scores through more expensive test-time search without changing its parameters or ability to adapt to an environment.

The research ledger therefore separates facts, interpretations, and hypotheses, and records how confidence changes.
