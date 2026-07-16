# How We Solve Distinct Subsequences

Count how many subsequences of `s` equal `t` with one-dimensional DP.

## Steps

1. Let `dp[j]` be ways to form the first `j` characters of `t`.
2. Seed `dp[0] = 1` for the empty prefix.
3. Scan each character of `s`.
4. Walk `t` backwards; when characters match, add `dp[j]` into `dp[j+1]`.
5. Return `dp[len(t)]`.
