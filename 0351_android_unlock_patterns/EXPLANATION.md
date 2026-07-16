# How We Solve Android Unlock Patterns

Bitmask DFS counts valid patterns with jump constraints on the 3x3 grid.

## Steps

1. Precompute jump middles for knight-like moves.
2. Allow a jump only when the middle cell is still empty.
3. Count corner, edge, and center starts with symmetry multipliers.
