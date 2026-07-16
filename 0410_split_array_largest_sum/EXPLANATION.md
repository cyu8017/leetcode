# How We Solve Split Array Largest Sum

Binary search the minimum feasible largest subarray sum.

## Steps

1. Search between max(nums) and sum(nums).
2. Greedily count how many parts a candidate limit needs.
3. Shrink the search until the smallest valid limit remains.
