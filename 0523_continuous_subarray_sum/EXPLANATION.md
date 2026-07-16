# How We Solve Continuous Subarray Sum

Prefix sums modulo k reveal repeated remainders at least two indices apart.

## Steps

1. Track the earliest index for each remainder of the running prefix sum.
2. If the same remainder appears again with gap ≥ 2, return true.
3. Handle `k = 0` using raw prefix values.
