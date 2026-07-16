# How We Solve Minimum Distance Between BST Nodes

Inorder traversal of a BST yields sorted values; track consecutive gaps.

## Steps

1. Walk the tree inorder.
2. Compare each value to the previous one.
3. Keep the minimum difference.
