# How We Solve New 21 Game

DP with a sliding window over the last `maxPts` draw probabilities.

## Steps

1. `dp[i]` = probability of reaching score `i` while still drawing.
2. Maintain the sum of `dp` over drawable prefixes `[i-maxPts, i)`.
3. Sum `dp[k..n]` for the answer (Alice stops at ≥ `k`).
