# How We Solve Inorder Successor in BST II

Use parent pointers without access to the root.

## Steps

1. If the node has a right subtree, return its leftmost node.
2. Otherwise climb parents while the node is a right child.
3. The parent after climbing is the successor, or null if none exists.
