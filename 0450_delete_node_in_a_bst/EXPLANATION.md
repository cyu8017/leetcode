# How We Solve Delete Node in a BST

Standard BST deletion with recursive search and inorder successor replacement.

## Steps

1. Recurse left or right until the key matches the current node.
2. If a child is missing, return the other child.
3. Otherwise copy the leftmost value from the right subtree and delete that successor node.
