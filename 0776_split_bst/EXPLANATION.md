# How We Solve Split BST

Recursively split into `≤ target` and `> target` trees.

## Steps

1. If root ≤ target, split the right subtree and attach the ≤ part as new right.
2. If root > target, split the left subtree and attach the > part as new left.
3. Return `[small, large]`.
