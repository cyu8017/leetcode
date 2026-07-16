# How We Solve Out of Boundary Paths

DP counts ways to stand on each cell after each move and tallies exits.

## Steps

1. Start with one way at the start cell.
2. For each move, spread ways to adjacent cells, adding out-of-bound transitions to the answer.
3. Reduce modulo `10^9 + 7`.
