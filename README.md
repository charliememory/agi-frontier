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

## Repository structure

The repository has two layers: `docs/` is the public research map and tutorial site; `experiments/`
contains the executable work that tests claims made in the docs.

```text
agi-frontier/
├── docs/
│   ├── index.md                 # Site home and the project's working thesis
│   ├── timeline/                # Technology path: how the prediction target expanded
│   ├── tutorials/               # Numbered learning units and the phase roadmap
│   ├── radar/                   # Current judgments and the research ledger
│   ├── experiments/             # Experiment conventions (optional)
│   ├── maintaining.md           # Language policy and publishing loop
│   ├── assets/                  # Site images and logo assets
│   ├── javascripts/             # Site-level JavaScript
│   ├── stylesheets/             # Site-level CSS tokens and overrides
│   └── overrides/               # MkDocs Material template overrides
├── experiments/
│   └── <id>-<slug>/              # Reproducible code, config, results, and failure cases
├── tests/                       # Content contracts and site-level regression checks
├── mkdocs.yml                   # Navigation, theme, Markdown extensions, and build config
├── pyproject.toml               # Python dependencies and tool configuration
└── uv.lock                      # Reproducible dependency lockfile
```

### Where to start

1. Read `docs/tutorials/index.md` for the question, phases, and current sprint.
1. Use `docs/timeline/index.md` when you want the historical order.
1. Read or write a tutorial in `docs/tutorials/`.
1. Experiments in `experiments/` are optional. Record changed judgments in the research ledger.

`docs/` is the source of truth for conclusions and public explanations. Model weights, datasets,
large logs, and generated site output stay out of Git; preserve configurations, metrics, failure
examples, and changed judgments instead.

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
