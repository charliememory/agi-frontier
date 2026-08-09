# Experiments

Experiments are the second leg of each tutorial. Keep them small enough to repeat on a limited budget while preserving interfaces that later methods can replace.

## Experiment tiers

| Tier       | Purpose                                      | Run mode                                       |
| ---------- | -------------------------------------------- | ---------------------------------------------- |
| `smoke`    | Check that code and configuration are intact | Run automatically on every pull request        |
| `repro`    | Reproduce a key curve or conclusion          | Trigger manually and save a result summary     |
| `frontier` | Expensive training or large-model evaluation | Run manually or overnight with a budget record |

## Directory convention

```text
experiments/<id>-<slug>/
  README.md
  config.yaml
  results.md
```

Model weights, datasets, and complete logs do not enter Git. The repository keeps configurations, code, metrics, an index of failure examples, and environment information.
