# How We Solve Construct Binary Tree from Preorder and Inorder Traversal

Rebuild a tree from preorder and inorder lists.

## Steps

1. The next preorder value is the current root.
2. Find that value in the inorder list to split left and right ranges.
3. Build the left subtree from the left range.
4. Build the right subtree from the right range.
5. Return the connected root.
