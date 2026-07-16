# How We Solve Trim a Binary Search Tree

Recursively drop nodes outside `[low, high]` using BST order.

## Steps

1. If root `< low`, keep only the trimmed right subtree.
2. If root `> high`, keep only the trimmed left subtree.
3. Otherwise trim both children and return root.
