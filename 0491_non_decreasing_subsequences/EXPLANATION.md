# How We Solve Non-decreasing Subsequences

Backtracking builds subsequences of length at least two while skipping duplicates at the same depth.

## Steps

1. Recurse from each start index, only appending non-decreasing values.
2. Skip repeated values at the same recursion level with a local set.
3. Collect subsequences of length ≥ 2 and return them sorted.
