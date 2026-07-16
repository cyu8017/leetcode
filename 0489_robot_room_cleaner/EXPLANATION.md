# How We Solve Robot Room Cleaner

DFS explores reachable cells using only move/turn APIs, backtracking to undo moves.

## Steps

1. Clean the current cell, then try all four directions.
2. Move forward when open, recurse, then reverse turns and move back.
3. Mark visited `(row, col, direction)` states to avoid cycles.
