# How We Solve Guess Number Higher or Lower II

Interval DP minimizes worst-case guessing cost.

## Steps

1. Fill dp[left][right] for every interval length.
2. Try each guess as the split point.
3. Add guess plus the worse side of the two subproblems.
