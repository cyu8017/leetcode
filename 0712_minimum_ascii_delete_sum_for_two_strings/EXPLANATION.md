# How We Solve Minimum ASCII Delete Sum for Two Strings

DP like edit distance, but only deletes, costing each character’s ASCII value.

## Steps

1. `dp[i][j]` = min delete cost to equalize `s1[:i]` and `s2[:j]`.
2. Equal chars carry `dp[i-1][j-1]` forward.
3. Otherwise delete from `s1` or `s2` and add that character’s cost.
