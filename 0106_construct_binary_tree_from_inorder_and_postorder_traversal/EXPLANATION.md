# How We Solve Construct Binary Tree from Inorder and Postorder Traversal

Rebuild a tree from inorder and postorder lists.

## Steps

1. The last unused postorder value is the current root.
2. Find that value in the inorder list to split ranges.
3. Build the right subtree first.
4. Then build the left subtree.
5. Return the connected root.
