# How We Solve Longest Continuous Increasing Subsequence

Scan for the longest strictly increasing contiguous run.

## Steps

1. Grow a streak while `nums[i] > nums[i-1]`.
2. Reset the streak on a non-increase.
3. Track the maximum streak length.
