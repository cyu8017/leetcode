# How We Solve Count Univalue Subtrees

Post-order DFS checks whether each subtree has a single value.

## Steps

1. Return true for null nodes.
2. Recursively verify the left and right subtrees.
3. Ensure child values match the current node when children exist.
4. If the whole subtree is unival, increment the counter.
5. Return whether the current subtree is unival.
