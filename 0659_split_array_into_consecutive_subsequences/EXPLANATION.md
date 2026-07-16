# How We Solve Split Array into Consecutive Subsequences

Greedy: prefer extending an existing chain of length ≥ 3; else start a new chain of three.

## Steps

1. Count frequencies; track how many subsequences end at each value (`tails`).
2. For each number, attach to a prior tail if possible.
3. Otherwise consume `num+1` and `num+2` to start a new subsequence, or fail.
