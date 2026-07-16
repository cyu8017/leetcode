# How We Solve Convert Sorted List to Binary Search Tree

Turn a sorted linked list into a height-balanced BST.

## Steps

1. Copy the list values into an array.
2. Pick the upper middle as the root.
3. Build left and right halves recursively.
4. Attach those subtrees to the root.
5. Return the balanced tree.
