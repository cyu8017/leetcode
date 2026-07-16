# How We Solve 01 Matrix

Multi-source BFS from every zero finds the nearest zero for each cell.

## Steps

1. Initialize distances to zero at all `0` cells and enqueue them.
2. Expand in four directions, updating neighbors with a shorter distance.
3. Return the completed distance matrix.
