# How We Solve Binary Trees With Factors

Sort values and DP: trees rooted at `x` = product of factor-pair trees.

## Steps

1. Sort `arr` ascending.
2. For each `x`, for each factor `left` with `right = x/left` in the set, add `dp[left]*dp[right]`.
3. Sum all `dp` values modulo `10^9+7`.
