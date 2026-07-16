# How We Solve The Maze III

Dijkstra on roll-stop states minimizes distance, breaking ties lexicographically on the path string.

## Steps

1. From each stop cell, roll in four directions until blocked or entering the hole.
2. Push `(distance, path, row, col)` states; skip dominated entries.
3. Return the path when the hole is reached, else `"impossible"`.
