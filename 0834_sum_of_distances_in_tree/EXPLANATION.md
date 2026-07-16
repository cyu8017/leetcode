# How We Solve Sum of Distances in Tree

Two DFS passes: subtree sums, then reroot to every node.

## Steps

1. Root at `0`; compute subtree sizes and distance sum for the root.
2. Reroot: `ans[child] = ans[parent] - size[child] + (n - size[child])`.
3. Return `ans` for all nodes.
