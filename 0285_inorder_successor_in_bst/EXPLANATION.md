# How We Solve Inorder Successor in BST

Use the right subtree minimum or the lowest ancestor on the left path.

## Steps

1. If the node has a right child, return the leftmost node in that subtree.
2. Otherwise walk from the root tracking the last node whose value is greater than p.
3. Return that successor or null if none exists.
