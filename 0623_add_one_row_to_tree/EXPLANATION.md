# How We Solve Add One Row to Tree

Insert new nodes as children of every node at depth `depth - 1`.

## Steps

1. If `depth == 1`, create a new root with the old tree on the left.
2. Otherwise DFS to depth `depth - 1`.
3. Rewire each node's left/right under freshly created `val` nodes.
