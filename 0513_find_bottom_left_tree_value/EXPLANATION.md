# How We Solve Find Bottom Left Tree Value

Level-order traversal keeps the first node seen on each row.

## Steps

1. BFS the tree level by level.
2. Record the first value in every level.
3. Return the last recorded value (deepest leftmost).
