# How We Solve Min Cost Climbing Stairs

DP from the top: each step costs itself plus the cheaper of the next one or two.

## Steps

1. Walk `cost` from the end, keeping two rolling values.
2. At each step, `a = cost[i] + min(a, b)`.
3. Answer is `min` of starting on step 0 or 1.
