# How We Solve Shortest Path Visiting All Nodes

BFS on `(node, visited_mask)` until the full mask is reached.

## Steps

1. Seed the queue with every node as a start (mask bit set).
2. Expand along graph edges, OR-ing the destination into the mask.
3. First time the mask is all ones is the shortest path length.
