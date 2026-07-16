# How We Solve Largest Sum of Averages

DP: best score for partitioning the prefix into `g` groups.

## Steps

1. Precompute prefix sums for O(1) range averages.
2. `dp[i]` = best with 1 group for `nums[0..i]`.
3. Transition by placing the last group ending at `i` after a previous best.
