# How We Solve Maximal Square

Use 1D DP where each cell stores the side length of the largest square ending there.

## Steps

1. Scan the matrix row by row with a rolling DP array.
2. When a cell is `1`, set `dp = min(left, top, top-left) + 1`.
3. Reset the cell to 0 when it is not part of a square.
4. Track the maximum side length seen.
5. Return its square area.
