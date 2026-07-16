# How We Solve Second Minimum Node In a Binary Tree

Root is the global minimum; search for the smallest value strictly larger than it.

## Steps

1. DFS the tree; when a node exceeds `root.val`, candidate-update and prune its subtree.
2. Keep exploring nodes equal to the root (children can diverge).
3. Return the best candidate, or `-1` if none.
