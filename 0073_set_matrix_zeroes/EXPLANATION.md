# How We Solve Set Matrix Zeroes

If a cell is 0, set its whole row and column to 0.

## Steps

1. Remember if the first row or column should become all zeros.
2. Use the first row and column as markers for other zeros.
3. Scan the rest of the grid and mark rows/columns that contain a zero.
4. Zero out marked rows and columns using the markers.
5. Fix the first row and column last if needed.
