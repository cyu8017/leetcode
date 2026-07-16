# How We Solve Longest Increasing Path in a Matrix

DFS with memoization finds the longest strictly increasing path.

## Steps

1. From each cell, explore four directions to higher neighbors.
2. Memoize the best path length starting at each cell.
3. Return the maximum over all starts.
