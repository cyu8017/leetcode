# How We Solve Clone Graph

DFS/BFS clone each node once and wire neighbor pointers to the clones.

## Steps

1. Return null for an empty graph.
2. Keep a map from original node value (or identity) to its clone.
3. Create the clone before recursing so cycles terminate.
4. Clone every neighbor and attach the cloned neighbor list.
5. Return the clone of the start node.
