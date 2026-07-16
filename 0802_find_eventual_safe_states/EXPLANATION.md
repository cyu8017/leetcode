# How We Solve Find Eventual Safe States

A node is safe iff every path ends in a terminal (no cycle reachable).

## Steps

1. 3-color DFS: visiting = gray, finished safe = black.
2. A gray revisit means a cycle → unsafe.
3. Collect all nodes that finish black.
