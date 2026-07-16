# How We Solve Insert into a Binary Search Tree

Walk the BST until an empty child slot matches the insert side.

## Steps

1. If the tree is empty, return a new root.
2. Compare `val` with the current node and move left/right.
3. Attach a new node at the first null child and return the original root.
