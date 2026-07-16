# How We Solve Shopping Offers

DFS with memoization over remaining needs, trying every special offer.

## Steps

1. Base cost is buying the remainder at unit prices.
2. For each offer that fits, recurse on the reduced needs.
3. Memoize states so overlapping subproblems are reused.
