# How We Solve Maximum Depth of N-ary Tree

DFS depth is one plus the deepest child subtree.

## Steps

1. Empty root has depth 0; a leaf has depth 1.
2. Recurse on every child and take the maximum.
3. Return `1 + max_child_depth`.
