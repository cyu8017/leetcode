# How We Solve House Robber II

The circle breaks into two linear house-robber problems.

## Steps

1. If there is one house, return its value.
2. Rob houses `0..n-2` with the classic linear DP.
3. Rob houses `1..n-1` with the same DP.
4. Track `prev2` and `prev1` while scanning each range.
5. Return the maximum of the two linear results.
