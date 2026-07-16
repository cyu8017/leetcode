# How We Solve The Maze II

Dijkstra on ball stop positions minimizes rolling distance to the destination.

## Steps

1. From each stop cell, roll in four directions until blocked.
2. Push `(distance, row, col)` into a min-heap for new stops.
3. Return the distance when the destination stop is reached, else `-1`.
