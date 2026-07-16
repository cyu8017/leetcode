# How We Solve Trapping Rain Water II

Min-heap BFS grows inward from the border water level.

## Steps

1. Push all border cells into a min-heap as the initial wall.
2. Pop the lowest cell and visit unvisited neighbors.
3. Trap water up to the current wall height and raise the wall inward.
