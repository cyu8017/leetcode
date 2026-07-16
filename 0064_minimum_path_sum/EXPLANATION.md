# How We Solve Minimum Path Sum

Find the cheapest path from top-left to bottom-right (only right or down).

## Steps

1. Use the grid itself to store the best cost so far.
2. Start at the top-left cell (cost stays the same).
3. Fill the first row by adding the cell to the left.
4. Fill the first column by adding the cell above.
5. For other cells, add the smaller of the costs from above or the left.
6. Return the bottom-right cell.
