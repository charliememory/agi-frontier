# Open Problems

Keep only questions that could plausibly be tested here; do not try to collect every open problem in the field.

## 1. When does a video model become an interactive world model?

Move beyond attractive video generation toward action-conditioned prediction, long-term state consistency, executable planning, and explicit failure boundaries.

**Minimal experiment**: in a simplified simulator, compare how pixel prediction, latent prediction, and true environment-state prediction affect planning.

## 2. Do VLAs need explicit long-term memory?

Success on short tasks does not imply success on tasks that span hours. Separate the contributions of memory, state estimation, planning, and action policy.

**Minimal experiment**: hold the policy fixed while changing only the history window, external memory, and task decomposer.

## 3. Can verifiers replace large-scale human feedback?

This can be tested in math, code, and simulated environments. Open-world and aesthetic tasks require studying verifier bias and incompleteness.

## 4. How can self-generated tasks avoid distribution collapse?

The task generator must keep finding tasks the model cannot solve but that can still be evaluated reliably, rather than repeating simple variants.

## 5. How can automated discovery prove that progress is real?

Keep an independent holdout, preregistered metrics, rollback versions, and a compute-budget record.
