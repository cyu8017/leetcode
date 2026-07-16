# How We Solve Lowest Common Ancestor of a BST

Use BST ordering to walk toward the split point.

## Steps

1. Start at the root.
2. If both target values are smaller, go left.
3. If both are larger, go right.
4. Otherwise the current node is the LCA.
5. Return that node.
