# How We Solve Number of Longest Increasing Subsequence

Track LIS length and how many ways each index reaches that length.

## Steps

1. `lengths[i]` / `counts[i]` for subsequences ending at `i`.
2. Extend from earlier smaller values; reset or add counts on ties.
3. Sum counts where length equals the global maximum.
