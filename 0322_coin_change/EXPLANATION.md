# How We Solve Coin Change

Bottom-up DP finds the minimum coins for each amount.

## Steps

1. Initialize dp[0] = 0 and others to infinity.
2. Relax each coin across all reachable amounts.
3. Return dp[amount] or -1 if unreachable.
