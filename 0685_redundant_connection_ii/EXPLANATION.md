# How We Solve Redundant Connection II

Handle a node with two parents separately from a pure directed cycle.

## Steps

1. If some node has two incoming edges, remember both candidates and drop the later one.
2. Union-Find the remaining edges; a cycle means return the earlier candidate (or the cycle edge).
3. If no cycle after dropping the later edge, that later edge is the answer.
