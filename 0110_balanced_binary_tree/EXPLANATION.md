# How We Solve Balanced Binary Tree

Check that every node's left and right heights differ by at most one.

## Steps

1. Compute height bottom-up.
2. If a subtree is already unbalanced, return a sentinel.
3. If left and right heights differ by more than 1, mark unbalanced.
4. Otherwise return 1 plus the larger child height.
5. The tree is balanced if the root height is not the sentinel.
