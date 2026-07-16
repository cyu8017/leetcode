# How We Solve Word Break

DP marks whether every prefix can be segmented with dictionary words.

## Steps

1. Put the dictionary into a set.
2. Let `dp[0]` mean the empty prefix is valid.
3. For each end index, try every earlier start where `dp[start]` is true.
4. If `s[start:end]` is a word, set `dp[end]`.
5. Return `dp[n]`.
