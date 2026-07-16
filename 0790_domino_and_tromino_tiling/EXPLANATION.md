# How We Solve Domino and Tromino Tiling

DP: `dp[i] = 2*dp[i-1] + dp[i-3]` (mod `10^9+7`).

## Steps

1. Base: `dp[1]=1`, `dp[2]=2`, `dp[3]=5`.
2. Recur with the closed form transition above.
3. Return `dp[n]`.
