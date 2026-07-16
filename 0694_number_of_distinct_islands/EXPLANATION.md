# How We Solve Number of Distinct Islands

Canonicalize each island as relative coordinates from its DFS start.

## Steps

1. Flood-fill every island, recording `(r-origin, c-origin)` cells.
2. Store shapes in a set of tuples.
3. The set size is the number of distinct islands.
