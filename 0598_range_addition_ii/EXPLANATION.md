# How We Solve Range Addition II

Every operation increments a prefix rectangle; the max cells are the intersection of all prefixes.

## Steps

1. Track the minimum `a` and minimum `b` across operations.
2. If there are no operations, the whole matrix stays at zero.
3. Return `min_a * min_b`.
