# How We Solve Unique Paths

Count paths from top-left to bottom-right moving only right or down.

## Steps

1. Use one row of counts, all starting at 1.
2. For each row below the first, update each cell.
3. Each cell adds the count from the cell above and the cell to the left.
4. The first row and column stay 1.
5. Return the bottom-right count in the row.
