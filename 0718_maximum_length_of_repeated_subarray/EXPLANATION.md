# How We Solve Maximum Length of Repeated Subarray

DP: longest common suffix ending at each pair of indices.

## Steps

1. If `nums1[i-1] == nums2[j-1]`, extend `dp[j-1] + 1`.
2. Otherwise the common suffix resets to 0.
3. Track the global maximum length (rolling 1D DP).
