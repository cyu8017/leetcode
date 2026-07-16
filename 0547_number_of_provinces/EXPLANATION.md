# How We Solve Number of Provinces

Connected cities in the adjacency matrix form provinces.

## Steps

1. Use union-find (or DFS) over city indices.
2. Union cities that are directly connected.
3. Count distinct connected components.
