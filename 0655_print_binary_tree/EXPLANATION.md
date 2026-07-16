# How We Solve Print Binary Tree

Place nodes into a matrix sized by height: `rows = h+1`, `cols = 2^{h+1}-1`.

## Steps

1. Compute tree height `h`.
2. Put root at the middle column of row 0.
3. Recursively place children at half the remaining horizontal offset each level.
