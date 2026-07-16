# How We Solve Coin Change II

Unbounded knapsack DP counts combinations for each amount.

## Steps

1. Initialize `dp[0] = 1`.
2. For each coin, add ways into larger amounts.
3. Return `dp[amount]`.
