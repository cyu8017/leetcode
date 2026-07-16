# How We Solve Maximum Product of Three Numbers

After sorting, the answer is either the three largest or the two smallest times the largest.

## Steps

1. Sort the array.
2. Compute `nums[-1] * nums[-2] * nums[-3]`.
3. Also compute `nums[0] * nums[1] * nums[-1]` and take the max.
