# How We Solve Sliding Puzzle

BFS over board states until `"123450"` or exhaustion.

## Steps

1. Serialize the 2×3 board as a string.
2. Swap `0` with its neighbors to generate moves.
3. Return the step count, or `-1` if unsolvable.
