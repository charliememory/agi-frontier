# External Resource Library

This library exists to keep the project honest. It records established courses, implementation
series, and talk archives that we can use as outside structure and comparison. It is intentionally
curated rather than exhaustive.

Checked: 2026-08-09. Links point to the official course, archive, or author page where possible.

## Recommended spine

| Resource | Format | Best use here | What we borrow | What we do not outsource |
| --- | --- | --- | --- | --- |
| [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/) | Course, code, assignments, recordings | Language-model foundations through alignment and reasoning | The implementation sequence: tokenizer → Transformer → systems → scaling → data → alignment | Our cross-modal, world-model, VLA, and self-improvement synthesis |
| [Andrej Karpathy — Zero to Hero](https://karpathy.ai/zero-to-hero.html) | Code-along video series | First-principles intuition and small runnable implementations | The “spell it out in code” teaching style | Its scope is neural nets/LLMs, not a complete AGI curriculum |
| [Stanford CS224N](https://web.stanford.edu/class/cs224n/) | Course, slides, assignments, public lecture playlist | NLP breadth, historical context, and research framing | Lecture sequencing and assignment-style learning objectives | We add explicit failure analysis and the AGI capability axes |

## Vision, generation, and multimodality

| Resource | Format | Use in roadmap |
| --- | --- | --- |
| [Stanford CS231n](https://cs231n.stanford.edu/) and [course notes](https://cs231n.github.io/) | Course, notes, assignments, lectures | Visual representation, transfer, self-supervision, captioning, and diffusion foundations |
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | Interactive tutorials | Practical Transformers, datasets, tokenizers, fine-tuning, and evaluation |
| [Hugging Face Diffusion Course](https://huggingface.co/learn/diffusion-course/unit0/1) | Interactive tutorials and notebooks | DDPM, latent diffusion, conditioning, and implementation of generative models |
| [Full Stack Deep Learning](https://fullstackdeeplearning.com/) | Lectures and project lifecycle material | Data, evaluation, deployment, monitoring, and the parts research demos often omit |

## Agents, reinforcement learning, and embodiment

| Resource | Format | Use in roadmap |
| --- | --- | --- |
| [Berkeley Deep Reinforcement Learning](https://rail.eecs.berkeley.edu/deeprlcourse/) | Lectures, calendar, notes, and resources | RL foundations, offline/online learning, planning, and policy evaluation |
| [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) | Modular course | Tool use, agent loops, traces, and practical evaluation |
| [Hugging Face Robotics Course](https://huggingface.co/learn/robotics-course) | Modular course and repository | Robot learning, datasets, policies, and VLA-adjacent implementation |

## Talks and research-frontier formats

| Resource | Format | Use in roadmap |
| --- | --- | --- |
| [Stanford CS25: Transformers United](https://web.stanford.edu/class/cs25/) and [recordings](https://web.stanford.edu/class/cs25/recordings/) | Research talk series | Discover current directions and learn how authors frame an open problem |
| [Stanford CS336 recordings](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV) | Full lecture sequence | Revisit difficult implementation and systems topics after running experiments |
| [Stanford CS224N 2024 lectures](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D) | Public lecture sequence | Compare a mature NLP course's explanation of LLMs and reasoning with our capability map |

Talks are for orientation, not evidence. A talk can suggest a hypothesis; a paper, artifact, and
independent test determine how strongly the radar should move.

## How to use this library without turning it into another backlog

For each tutorial, select:

1. one anchor course or implementation sequence;
2. one primary paper that introduced the mechanism;
3. one talk that exposes the current frontier or disagreement.

Record the selection in the tutorial's `Anchor sources` section. Do not assign every resource to
every tutorial. The point is triangulation: a pedagogical course, a primary source, and a current
research conversation should disagree in useful ways.

## Resource review card

When adding a new course, tutorial, or talk archive, use this small card:

```markdown
### Resource title

**URL**:
**Type**: course / tutorial / talk / notes / code
**Maintainer and last visible update**:
**Roadmap phases**:
**What is unusually good**:
**What it omits or assumes**:
**One artifact worth borrowing**:
**Evidence checked**: official page / public code / recordings / other
```
