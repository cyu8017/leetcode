# How We Solve Combination Sum IV

Order-sensitive DP counts ways to reach each target amount.

## Steps

1. Set dp[0] = 1.
2. For each amount, add dp[amount - num] across all nums.
3. Return dp[target].
