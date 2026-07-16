# How We Solve Closest Binary Search Tree Value

Walk the BST while tracking the closest value seen so far.

## Steps

1. Start with the root value as the closest candidate.
2. Compare distance to the current node and update if closer.
3. Return immediately on an exact match.
4. Go left if the target is smaller, otherwise go right.
5. Return the closest value after the walk ends.
