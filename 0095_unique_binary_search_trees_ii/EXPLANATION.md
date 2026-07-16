# How We Solve Unique Binary Search Trees II

Build every unique BST that stores values 1 through n.

## Steps

1. For a number range, try each value as the root.
2. Build all left subtrees from smaller values.
3. Build all right subtrees from larger values.
4. Pair every left tree with every right tree.
5. Collect all roots formed that way.
