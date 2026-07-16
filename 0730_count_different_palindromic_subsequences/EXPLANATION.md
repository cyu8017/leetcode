# How We Solve Count Different Palindromic Subsequences

Interval DP counting distinct palindromic subsequences modulo `10^9+7`.

## Steps

1. `dp[i][j]` = distinct palindromic subsequences in `s[i..j]`.
2. When ends differ, combine the two smaller intervals minus the overlap.
3. When ends match, double the inner count and adjust for duplicate bounding letters.
