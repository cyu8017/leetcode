# How We Solve Binary Tree Vertical Order Traversal

BFS groups nodes by column while preserving left-to-right order.

## Steps

1. Queue nodes with their column index starting at root column 0.
2. Append values to each column list in BFS order.
3. Return columns from min to max index.
