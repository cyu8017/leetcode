# How We Solve K Inverse Pairs Array

DP counts arrays of size `n` with exactly `k` inversions using a sliding window sum.

## Steps

1. Let `dp[k]` be ways to form exactly `k` inversions with the current size.
2. When inserting `n`, it can create `0..n-1` new inversions.
3. Maintain a prefix window so each transition is O(1) modulo `10^9+7`.
