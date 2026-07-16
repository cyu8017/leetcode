# How We Solve Largest BST Subtree

Post-order DFS returns BST validity, min, max, and subtree size.

## Steps

1. Empty nodes are valid BSTs with neutral bounds.
2. Merge left and right info when values satisfy BST ordering.
3. Track the maximum valid subtree size seen.
