# AGI Frontier

A public learning and experimentation project for researchers and engineers. It starts with token prediction and follows the shared path through multimodal understanding, generative models, world models, VLAs, and self-improving agents.

> Reading is not the finish line. Every judgment should lead to an experiment, a failure case, or a falsifiable hypothesis.

## Run locally

Requires Python 3.12+.

```bash
uv sync
uv run mkdocs serve
```

Open `http://127.0.0.1:8000/agi-frontier/` to preview the site.

## Content conventions

- `docs/` is the single source of truth for public content.
- `experiments/` stores reproducible small experiments, configurations, and result summaries.
- Each tutorial answers: question, mechanism, minimal implementation, controlled comparison, failure modes, current judgment, and next test.
- Separate facts, interpretations, and hypotheses; do not turn a paper abstract into a personal conclusion.
- English is the canonical language. Translations, when added, should mirror the English page without changing its scope or evidence level.

## Contributing

Use Issues to suggest papers, counterexamples, and reproduction ideas. Submit substantive changes through pull requests; CI checks the site build and basic Markdown quality.

## License

Licensing for content and code will be selected once the first tutorial set stabilizes. Until then, preserve the copyright notices for papers and third-party resources.
