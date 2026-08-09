# Experiments

实验是 tutorial 的第二条腿。每个实验尽量小到可以在有限预算下重复，但保留能被后来方法替换的接口。

## 实验分级

| 等级 | 目的 | 运行方式 |
| --- | --- | --- |
| `smoke` | 检查代码和配置没有坏 | 每个 Pull Request 自动运行 |
| `repro` | 复现关键曲线或结论 | 手动触发，保存结果摘要 |
| `frontier` | 昂贵训练或大模型评测 | 手动/夜间运行，记录预算 |

## 目录约定

```text
experiments/<id>-<slug>/
  README.md
  config.yaml
  results.md
```

模型权重、数据集和完整日志不进入 Git；仓库保留配置、代码、指标、失败样例索引和环境信息。

