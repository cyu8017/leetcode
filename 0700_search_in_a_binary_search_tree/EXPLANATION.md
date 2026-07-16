# How We Solve Search in a Binary Search Tree

Walk left/right by BST order until the value is found or the path ends.

## Steps

1. While the current node exists and differs from `val`, go left or right.
2. Return the node (subtree root) or `null`.
