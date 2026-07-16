# How We Solve Diameter of Binary Tree

The diameter is the longest path between any two nodes measured in edges.

## Steps

1. Recursively compute each node's left and right subtree depths.
2. At each node, update the best answer with `leftDepth + rightDepth`.
3. Return the maximum diameter found.
