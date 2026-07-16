# How We Solve Positions of Large Groups

Scan consecutive equal-letter runs; keep those of length ≥ 3.

## Steps

1. Two pointers expand each same-character group.
2. If `end - start + 1 >= 3`, record `[start, end]`.
3. Groups are already in start-index order.
