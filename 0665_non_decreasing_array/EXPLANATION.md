# How We Solve Non-decreasing Array

Allow at most one change when a descent appears.

## Steps

1. Scan for `nums[i] < nums[i-1]`.
2. On the first descent, either raise `nums[i]` or lower `nums[i-1]` based on `nums[i-2]`.
3. A second descent fails.
