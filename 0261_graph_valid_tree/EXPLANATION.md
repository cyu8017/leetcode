# How We Solve Graph Valid Tree

A valid tree on n nodes has exactly n-1 edges and no cycles.

## Steps

1. Reject immediately if the edge count is not n-1.
2. Initialize union-find parent pointers for each node.
3. For each edge, find the roots of both endpoints.
4. If the roots match, a cycle exists.
5. Otherwise merge the components and return true at the end.
