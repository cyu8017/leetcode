# How We Solve Is Graph Bipartite?

2-color the graph with DFS/BFS; fail on a same-color edge.

## Steps

1. For each uncolored component, color the start node.
2. Assign neighbors the opposite color.
3. Return false if a neighbor already has the same color.
