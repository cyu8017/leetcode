# How We Solve Swim in Rising Water

Dijkstra on grid cells: cost to enter a cell is the max height seen on the path.

## Steps

1. Priority-queue from `(0,0)` by current time (= max height so far).
2. Move to neighbors with `new_time = max(time, grid[nr][nc])`.
3. First time reaching the bottom-right is optimal.
