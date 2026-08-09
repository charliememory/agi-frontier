# Frontier Radar

This page records developments that change a judgment, not every piece of news. Each entry carries an evidence level and a next validation step.

## Current focus

### World models

Video generation is moving from “looks plausible” toward predicting future states and constructing interactive environments. The key tests are not single-frame quality, but object permanence, action-conditioned prediction, long-horizon consistency, and state representations useful for planning.

### VLA

VLAs place visual observations, language tasks, and action sequences in one loop. The main bottlenecks remain data coverage, cross-embodiment generalization, failure recovery, and safe online learning.

### Verifiers

Test-time compute and self-improving systems share the same foundation: reliable evaluators. Without independent holdouts, rollback mechanisms, and anti-reward-hacking tests, “self-improvement” may only be self-confirmation.

## Evidence levels

`L0` launch claim · `L1` paper experiment · `L2` public-code reproduction · `L3` independent reproduction · `L4` long-term deployment feedback

Do not treat `L0` as a capability conclusion.

## Update cadence

Write one short memo each month: which judgment changed, what the evidence was, and what to validate next month. Start by using GitHub Watch; add an RSS/Atom feed once the publishing cadence is stable.
