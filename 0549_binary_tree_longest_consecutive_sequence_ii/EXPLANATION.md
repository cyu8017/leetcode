# How We Solve Binary Tree Longest Consecutive Sequence II

Consecutive paths may go down with difference `+1` or `-1`, including through the parent.

## Steps

1. DFS each node for longest increasing and decreasing chains in its subtrees.
2. Combine left and right chains through the parent when values differ by one.
3. Track the maximum path length anywhere in the tree.
