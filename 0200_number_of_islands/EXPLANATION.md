# How We Solve Number of Islands

DFS/BFS flood-fill every land cell and count how many components you start.

## Steps

1. Scan the grid for an unvisited `'1'`.
2. Increment the island count.
3. Flood-fill that component, marking land as water.
4. Continue scanning for the next unvisited land cell.
5. Return the total number of islands.
