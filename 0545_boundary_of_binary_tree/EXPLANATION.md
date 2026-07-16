# How We Solve Boundary of Binary Tree

The boundary is root, left edge, leaves left-to-right, then right edge reversed.

## Steps

1. Collect the root and traverse the left boundary down non-leaf nodes.
2. Gather all leaf values inorder.
3. Append the right boundary values from bottom to top.
