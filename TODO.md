# AGI Frontier Curriculum TODO

This document turns the long-term roadmap into an executable self-learning system. The 24 tutorials
remain a map of the field; the `Core / Bridge / Frontier` layers determine how deeply and when each
topic is studied.

## Framework decision

- **Core** builds concepts that are required to reason about later systems.
- **Bridge** connects those concepts across language, perception, generation, and action.
- **Frontier** tracks unstable research questions and should change as evidence changes.
- A topic enters the permanent curriculum because it explains a durable mechanism, not because a
    model release is currently popular.
- Experiments may follow the conceptual design. A tutorial can begin before its full implementation
    exists, but it is not complete until it leaves an evidence-bearing artifact.

## Current SFT and RL coverage

- [x] SFT is present in Tutorial 03, **Supervised fine-tuning, preference optimization, and
    language-model RL**.
- [x] Preference feedback appears in the shared learning loop.
- [x] Imitation learning, policies, and online adaptation appear in Phase IV.
- [x] Berkeley Deep Reinforcement Learning is listed as an external anchor.
- [x] Make the scope of Tutorial 03 explicit: SFT, reward or preference modeling, direct preference
    optimization, RLHF, and reinforcement learning from verifiable feedback.
- [x] Add a durable RL foundations bridge before the agent and VLA material. It should cover MDPs,
    return and credit assignment, policy and value methods, model-free versus model-based RL,
    offline versus online RL, exploration, and evaluation.
- [x] Explain the relationship and differences between language-model post-training RL and embodied
    or sequential-control RL.
- [x] Keep RL foundations as a standalone Core bridge and keep Tutorial 16 focused on imitation
    learning, action representations, and diffusion policies.

## Proposed curriculum layers

### Core: understand deeply and assess directly

- 00 - Orientation and the shared learning loop.
- 01 - Transformer and language modeling.
- 02 - Scaling laws, data, and compute.
- 03 - SFT, preference optimization, RLHF, and verifiable-reward learning.
- 04 - Reasoning, search, test-time compute, and verifiers.
- 05 - Retrieval, memory, and long context.
- Required prerequisite bridge - RL foundations and sequential decision-making.

**Core exit criterion:** explain each mechanism without notes, compare it with at least one
alternative, identify a failure boundary, and state what evidence would change the current judgment.

### Bridge: connect previously learned mechanisms

- 06-09 - Visual and multimodal representation.
- 10-14 - Generative models, video prediction, and world models.
- 15-18 - Agents, policy learning, VLAs, planning, memory, and adaptation.

**Bridge exit criterion:** trace a failed system across representation, prediction, evaluation, and
action, rather than attributing the failure to the model as a whole.

### Frontier: maintain judgments rather than claim mastery

- 19-23 - Synthetic data, verifiers, research agents, discovery loops, and safety.
- Monthly radar topics that have not yet earned a permanent place in the roadmap.

**Frontier exit criterion:** produce a dated judgment memo that separates reported claims, public
evidence, independent evidence, open disagreement, and the next useful validation.

## P0 - Curriculum architecture

- [ ] Add `Core / Bridge / Frontier` labels to the roadmap without deleting the existing five-phase
    domain structure. The layers describe learning depth; the phases describe subject matter.
- [x] Resolve the RL gap described above and record the decision in the roadmap.
- [ ] Add prerequisites and exit criteria to every Core tutorial.
- [ ] Define the minimum learning artifact for every tutorial:
    - a mechanism explanation in the learner's own words;
    - a comparison with a predecessor or alternative;
    - one failure boundary or falsification plan;
    - one dated judgment update.
- [ ] Make the current sprint explicit. Multiple Core tutorials may be `in progress`; use AI-assisted
    coding to move at least one reviewable learning artifact forward every week, and record the next
    deliverable for every active tutorial.
- [ ] Add a time budget to each Core tutorial, initially targeting one week and 6-8 focused hours.

## P1 - External-course crosswalk

- [ ] Use Stanford CS336 to identify which Core topics need assignment-style checks and explicit
    compute requirements.
- [ ] Use Karpathy's Zero to Hero pattern for time-boxed, from-scratch mechanism walkthroughs. Borrow
    the artifact discipline, not its exact syllabus.
- [ ] Use the Hugging Face course pattern for low-friction runnable entry points, short knowledge
    checks, and a visible weekly workload. Keep library usage separate from from-scratch understanding.
- [ ] Use Full Stack Deep Learning selectively for evaluation, experiment management, and project
    walkthroughs. Defer deployment and monitoring until the course produces systems worth deploying.
- [ ] For every Core tutorial, select one pedagogical anchor, one primary source, and one current
    disagreement. Record what each source contributes and omits.
- [x] Add the initial reading list below. Keep it as an entry route into each topic, not a second
    syllabus that must be completed end to end.

## Reading list by course segment

Use the **anchor** to learn the sequence, the **primary sources** to inspect the mechanism and
evidence, and the **reading question** to produce a judgment rather than a summary. Start with one
anchor and one primary source; add more only when a comparison or unresolved question requires it.

| Tutorials                                  | External anchor                                                                                                                                 | Primary reading                                                                                                                                                                               | Reading question                                                                                     |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 00-01 · Orientation and Transformer        | [Stanford CS336](https://cs336.stanford.edu/) · [Karpathy Zero to Hero](https://karpathy.ai/zero-to-hero.html)                                  | [Attention Is All You Need](https://arxiv.org/abs/1706.03762)                                                                                                                                 | Which bottleneck did attention remove, and which limits of prediction remained?                      |
| 02 · Scaling, data, and compute            | [Stanford CS336](https://cs336.stanford.edu/)                                                                                                   | [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) · [Chinchilla](https://arxiv.org/abs/2203.15556)                                                                  | Under a fixed budget, when should capacity go to parameters, data, or optimization?                  |
| 03 · SFT, preferences, language-model RL   | CS336 alignment material · [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)                                        | [InstructGPT](https://arxiv.org/abs/2203.02155) · [DPO](https://arxiv.org/abs/2305.18290) · [DeepSeek-R1](https://arxiv.org/abs/2501.12948)                                                   | Which gain comes from demonstrations, preference data, reward design, or additional optimization?    |
| 04 · Reasoning, search, test-time compute  | CS336 reasoning material · [Stanford CS25](https://web.stanford.edu/class/cs25/)                                                                | [Tree of Thoughts](https://arxiv.org/abs/2305.10601) · [Scaling LLM Test-Time Compute](https://arxiv.org/abs/2408.03314)                                                                      | Is capability located in model weights, inference search, the verifier, or their interaction?        |
| 05 · Retrieval, memory, long context       | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)                                                                   | [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) · [Lost in the Middle](https://arxiv.org/abs/2307.03172)                                                                   | When does external memory improve reliability, and when does it add another failure surface?         |
| RL Core bridge · Sequential decisions      | [Berkeley Deep RL](https://rail.eecs.berkeley.edu/deeprlcourse/) · [OpenAI Spinning Up](https://spinningup.openai.com/en/latest/)               | [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html) · [DQN](https://arxiv.org/abs/1312.5602) · [PPO](https://arxiv.org/abs/1707.06347)               | How do credit assignment, exploration, and distribution shift change the learning problem?           |
| 06-09 · Vision and multimodal grounding    | [Stanford CS231n](https://cs231n.stanford.edu/)                                                                                                 | [CLIP](https://arxiv.org/abs/2103.00020) · [BLIP-2](https://arxiv.org/abs/2301.12597) · [LLaVA](https://arxiv.org/abs/2304.08485)                                                             | Is a failure caused by perception, alignment, spatial structure, or language reasoning?              |
| 10-12 · Diffusion and controllability      | [Hugging Face Diffusion Course](https://huggingface.co/learn/diffusion-course/unit0/1)                                                          | [DDPM](https://arxiv.org/abs/2006.11239) · [Latent Diffusion](https://arxiv.org/abs/2112.10752) · [DiT](https://arxiv.org/abs/2212.09748) · [Flow Matching](https://arxiv.org/abs/2210.02747) | How do representation, objective, and sampler trade off fidelity, speed, and control?                |
| 13-14 · Video and world models             | [Stanford CS25](https://web.stanford.edu/class/cs25/)                                                                                           | [World Models](https://arxiv.org/abs/1803.10122) · [DreamerV3](https://arxiv.org/abs/2301.04104) · [Genie](https://arxiv.org/abs/2402.15391)                                                  | What evidence is required before a video predictor deserves to be called a world model?              |
| 15 · Tool-using agents                     | [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction)                                                     | [ReAct](https://arxiv.org/abs/2210.03629) · [Toolformer](https://arxiv.org/abs/2302.04761)                                                                                                    | Which failures are reduced by typed tools, traces, budgets, and recovery policies?                   |
| 16 · Imitation and diffusion policies      | [Hugging Face Robotics Course](https://huggingface.co/learn/robotics-course)                                                                    | [Diffusion Policy](https://arxiv.org/abs/2303.04137) · [ACT](https://arxiv.org/abs/2304.13705)                                                                                                | Which action representation works under multimodality, limited demonstrations, and embodiment shift? |
| 17-18 · VLA, planning, memory, adaptation  | [Hugging Face Robotics Course](https://huggingface.co/learn/robotics-course) · [Berkeley Deep RL](https://rail.eecs.berkeley.edu/deeprlcourse/) | [RT-2](https://arxiv.org/abs/2307.15818) · [Open X-Embodiment](https://arxiv.org/abs/2310.08864)                                                                                              | Is failure caused by perception, planning, control, data coverage, memory, or recovery?              |
| 19 · Synthetic data and curricula          | [Berkeley Deep RL](https://rail.eecs.berkeley.edu/deeprlcourse/)                                                                                | [Self-Instruct](https://arxiv.org/abs/2212.10560) · [Automatic Curriculum Learning for Deep RL](https://arxiv.org/abs/2007.11971)                                                             | Can generated tasks stay diverse, evaluable, and near the capability boundary?                       |
| 20 · Verifiers and process supervision     | CS336 reasoning material · [Stanford CS25](https://web.stanford.edu/class/cs25/)                                                                | [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) · [DeepSeek-R1](https://arxiv.org/abs/2501.12948)                                                                               | How should false positives, reward hacking, and held-out transfer be measured?                       |
| 21-23 · Research agents, discovery, safety | [Full Stack Deep Learning](https://fullstackdeeplearning.com/) for evaluation discipline                                                        | [The AI Scientist](https://arxiv.org/abs/2408.06292) · [Constitutional AI](https://arxiv.org/abs/2212.08073)                                                                                  | What counts as real improvement when the system also influences the search process or evaluator?     |

### Reading workflow

- [ ] Before reading, write the current answer to the segment's reading question and a confidence
    level.
- [ ] For each Core segment, record one anchor, one primary source, and one genuine disagreement in
    the relevant tutorial.
- [ ] After reading, record the mechanism, strongest evidence, evaluation boundary, and whether the
    prior judgment changed.
- [ ] Prefer original papers and public artifacts over later summaries when their claims differ.
- [ ] Add a source only when it changes the explanation, comparison, failure analysis, or next test.

## P1 - Learning cadence and accountability

- [ ] Adopt a weekly cycle:
    - define one question and the prior belief;
    - study and reconstruct the mechanism;
    - compare competing explanations or methods;
    - record confusion, failure boundaries, and the next test;
    - publish one dated artifact.
- [ ] Use AI-assisted coding to iterate learning artifacts weekly. Explanation, implementation,
    controlled comparison, evaluation, and failure logs may advance in parallel rather than waiting
    for a tutorial to be complete in one pass.
- [ ] Publish one research-ledger update at least every two weeks, including weeks where the judgment
    did not change.
- [ ] At the end of each Core tutorial, perform a closed-notes explanation and answer five retrieval
    questions before moving on.
- [ ] At each phase checkpoint, write a synthesis across tutorials instead of another isolated
    summary.
- [ ] Review the roadmap once per quarter. Do not restructure it in response to every model release.

## P2 - Information architecture

- [ ] Make the four-part loop the primary operating model:
    `Represent -> Predict -> Evaluate/Act -> Improve`.
- [ ] Present the five capability axes as evaluation dimensions applied to that loop, not as a second
    competing roadmap.
- [ ] Present the five phases as domain progression and the three curriculum layers as depth and
    scheduling. Add one diagram or table that shows this relationship.
- [ ] Replace broad homepage focus labels with the active Core sprint plus long-term frontier
    interests.
- [ ] Add visible status values: `not started`, `in progress`, `concept complete`, `evidence added`,
    and `revisit`.

## P2 - Evidence and assessment

- [ ] Separate conceptual completion from empirical completion so implementation can follow without
    making unfinished evidence look complete.
- [ ] Define evidence-bearing artifacts by topic: derivation, code, controlled experiment, evaluation
    suite, literature comparison, or judgment memo.
- [ ] Require every strong claim to link to an evidence level and state its evaluation boundary.
- [ ] Add machine-checkable completion rules only after the conceptual contract stabilizes.
- [ ] Revisit every Core judgment after the relevant Bridge material exposes new assumptions.

## Deferred intentionally

- [ ] Complete experiment implementations after the associated conceptual comparison is stable.
- [ ] Expand translation only after a page is stable and actively used.
- [ ] Add community forums, certificates, or contribution workflows only after external learners
    create real demand.
- [ ] Add deployment and monitoring material only when it supports a concrete learning question.
- [ ] Promote a Frontier topic into Core or Bridge only after it demonstrates durable explanatory
    value across multiple systems.

## Next three actions

1. Add layer labels, prerequisites, exit criteria, and time budgets to Tutorials 00-05.
1. Start the first one-week Core cycle with Tutorial 01 and publish the first dated judgment update.
1. Select the pedagogical anchor, primary source, and current disagreement for Tutorial 02.
