# How We Solve Closest Leaf in a Binary Tree

Build an undirected graph of the tree, then BFS from `k` to the nearest leaf.

## Steps

1. Link each node to its parent and children.
2. BFS from `k`; the first leaf reached is closest.
3. Return that leaf’s value.
