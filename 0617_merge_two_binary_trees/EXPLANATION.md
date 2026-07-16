# How We Solve Merge Two Binary Trees

Recursively sum overlapping nodes and reuse whichever child is non-null.

## Steps

1. If either root is null, return the other.
2. Add the two node values into `root1`.
3. Recurse on left and right child pairs.
