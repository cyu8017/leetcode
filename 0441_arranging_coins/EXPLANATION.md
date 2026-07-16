# How We Solve Arranging Coins

Find the largest complete staircase row count whose triangular sum fits in `n`.

## Steps

1. Binary search on the answer `k` in `[0, n]`.
2. Check whether `k * (k + 1) / 2` is at most `n`.
3. Return the maximum valid `k`.
