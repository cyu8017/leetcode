# How We Solve Arithmetic Slices II - Subsequence

Dynamic programming counts arithmetic subsequences ending at each index per difference.

## Steps

1. For each pair `(j, i)`, compute difference `nums[i] - nums[j]`.
2. Add prior counts for that difference at `j` to the answer.
3. Extend the DP map at `i` with new length-2 and longer subsequences.
