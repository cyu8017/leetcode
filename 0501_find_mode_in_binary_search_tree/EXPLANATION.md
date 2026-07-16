# How We Solve Find Mode in Binary Search Tree

Inorder traversal of a BST counts value frequencies.

## Steps

1. Walk the tree inorder, updating a frequency map.
2. Track the maximum frequency seen.
3. Return every value whose count equals that maximum.
