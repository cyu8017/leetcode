# How We Solve Split Array With Same Average

Need a nonempty proper subset with average equal to the whole array’s average.

## Steps

1. Equivalent: subset size `k` with sum `total*k/n` (integer).
2. For each feasible `k`, DFS/DP search for that sum.
3. Return true on the first hit.
