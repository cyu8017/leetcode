# How We Solve Network Delay Time

Dijkstra from node `k`; answer is the max distance if all nodes are reached.

## Steps

1. Build the weighted adjacency list.
2. Run Dijkstra to get shortest times to every node.
3. Return the maximum time, or `-1` if some node is unreachable.
