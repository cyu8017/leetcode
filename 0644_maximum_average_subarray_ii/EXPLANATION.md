# How We Solve Maximum Average Subarray II

Binary-search the average and check for a subarray of length ≥ `k` with that mean.

## Steps

1. Search mid values between `min(nums)` and `max(nums)`.
2. Transform to `nums[i] - mid` and look for a non-negative prefix window of length ≥ `k`.
3. Raise or lower the candidate average accordingly.
