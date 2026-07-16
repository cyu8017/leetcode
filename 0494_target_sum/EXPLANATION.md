# How We Solve Target Sum

Convert ± assignments into counting subsets with a fixed positive sum.

## Steps

1. Check parity and bounds; let `need = (sum(nums) + target) / 2`.
2. DP counts ways to reach each subset sum.
3. Return `dp[need]`.
