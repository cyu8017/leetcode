# How We Solve N-Queens II

Count how many ways to place n queens on an n×n board safely.

## Steps

1. Place queens one row at a time.
2. For each row, try every column.
3. Skip a column if another queen shares the same column or diagonal.
4. When all rows are filled, add 1 to the count.
5. Backtrack and try other columns.
6. Return the total count.
