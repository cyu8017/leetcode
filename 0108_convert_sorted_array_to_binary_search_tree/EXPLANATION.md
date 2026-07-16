# How We Solve Convert Sorted Array to Binary Search Tree

Turn a sorted array into a height-balanced BST.

## Steps

1. Pick the middle value as the root (use the upper middle).
2. Recursively build the left half as the left subtree.
3. Recursively build the right half as the right subtree.
4. Connect them to the root.
5. Repeat until the range is empty.
