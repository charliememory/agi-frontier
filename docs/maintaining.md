# Maintaining the Site

The first phase optimizes for learning velocity and judgment quality, not translation coverage.

## Language policy

- English is the canonical language for every tutorial, radar entry, experiment summary, and navigation label.
- Do not block an English update on a translation.
- Add Chinese only when a page has stabilized and the translation provides clear value for readers.
- A translation should link to its English source and record the source revision or date.
- If the two versions disagree, the English page is authoritative until the difference is resolved.

## Suggested translation layout

When the audience justifies a second language, use a parallel path rather than bilingual paragraphs:

```text
docs/
  en/   # canonical pages, if the site grows beyond one language
  zh/   # translated pages with matching slugs
```

The current single-language layout deliberately avoids that migration cost. Revisit it only when there are enough translations to justify language navigation and separate search indexes.

## Publishing loop

1. Open an Issue with the question, evidence, and proposed experiment.
1. Read and reproduce the smallest useful slice.
1. Update the relevant tutorial, radar entry, or research-ledger memo.
1. Open a pull request and let CI run formatting, tests, links, and the strict site build.
1. Publish only after the page states its evidence level and next validation step.

## Research protocol

The repository uses a compact reading-and-reproduction protocol. It belongs to maintenance rather
than the numbered tutorial sequence because it describes how to learn, not a technical mechanism.

### Four passes

1. **Claim:** what changed, against which baseline, data, tools, and compute?
1. **Mechanism:** what changed in representation, prediction, feedback, or the improvement loop?
1. **Evidence:** are evaluation data independent, comparisons fair, and evaluators game-resistant?
1. **Reproduction:** what smallest experiment could change the current judgment?

### Evidence ladder

| Level | Meaning                                            | Permitted conclusion                            |
| ----- | -------------------------------------------------- | ----------------------------------------------- |
| `L0`  | Announcement, demo, or selected examples           | Monitor only                                    |
| `L1`  | Paper or technical report experiment               | Authors report the result under their setup     |
| `L2`  | Public artifacts reproduce the central result      | Reproducible in one disclosed setup             |
| `L3`  | Independent reproduction or adversarial evaluation | Robust beyond the originating team              |
| `L4`  | Long-term uncontrolled use                         | Operational reliability and limits are observed |

### Tutorial completion contract

Every tutorial should leave behind a mechanism summary, minimal implementation, controlled
comparison, three concrete failures, fact/interpretation/hypothesis separation, a ledger update,
and a falsifiable next experiment.

## Keeping it sustainable

Prefer one strong update per month over a daily news feed. Keep large model weights, datasets, and raw logs outside Git; preserve configurations, metrics, failure examples, and changed judgments in the repository.
