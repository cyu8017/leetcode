# How We Solve Shortest Distance from All Buildings

BFS from each building accumulates distance and reach counts on empty cells.

## Steps

1. For every building, BFS across empty land cells.
2. Add distance and increment reach count per cell.
3. Return the minimum distance among cells reached by all buildings.
