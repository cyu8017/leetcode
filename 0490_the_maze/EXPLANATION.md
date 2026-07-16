# How We Solve The Maze

Model the ball rolling until it hits a wall, then DFS/BFS on stop positions.

## Steps

1. From each cell, slide in four directions until the next cell is blocked.
2. Mark stop cells visited to prevent repeats.
3. Return true if the destination stop is reachable.
