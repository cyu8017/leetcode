# How We Solve Max Increase to Keep City Skyline

Each building can rise to `min(row_max, col_max)` without changing skylines.

## Steps

1. Compute max of every row and column.
2. For each cell, add `min(rowMax, colMax) - height`.
3. Sum those increases.
