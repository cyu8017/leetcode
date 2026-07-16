# How We Solve Maximum Sum of 3 Non-Overlapping Subarrays

Precompute window sums; pick a middle window and best non-overlapping left/right.

## Steps

1. Build length-`k` window sums.
2. Prefix-best and suffix-best indices for those windows.
3. Enumerate the middle start; choose the lexically smallest triple with max total.
