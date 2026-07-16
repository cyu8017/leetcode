# How We Solve Predict the Winner

Interval DP stores the score difference the current player can guarantee.

## Steps

1. Base case: single pile gives that pile's value.
2. For wider intervals, take max of picking left or right minus opponent's best reply.
3. Player 1 wins if `dp[0][n-1] >= 0`.
