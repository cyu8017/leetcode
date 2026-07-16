# How We Solve Find the Derangement of An Array

Use the recurrence `!n = (n - 1) * (!(n - 1) + !(n - 2))` modulo `10^9+7`.

## Steps

1. Base cases: `!1 = 0`, `!2 = 1`.
2. Iterate up to `n` with two rolling variables.
3. Reduce every step modulo `10^9+7`.
