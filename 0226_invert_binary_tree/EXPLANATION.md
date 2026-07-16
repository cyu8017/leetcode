# How We Solve Invert Binary Tree

Recursively swap each node's left and right children.

## Steps

1. Return null for an empty tree.
2. Recursively invert the right subtree.
3. Recursively invert the left subtree.
4. Assign the inverted right subtree to `left`.
5. Assign the inverted left subtree to `right`.
