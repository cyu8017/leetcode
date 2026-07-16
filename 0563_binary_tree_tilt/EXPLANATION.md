# How We Solve Binary Tree Tilt

Post-order DFS returns subtree sums while accumulating absolute left/right differences.

## Steps

1. Recurse to get left and right subtree sums.
2. Add `|left - right|` to the answer.
3. Return `node.val + left + right` to the parent.
