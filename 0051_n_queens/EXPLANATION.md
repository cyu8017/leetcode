# How We Solve N-Queens

Place n queens on an n×n board so no two attack each other.

## Steps

1. Place queens one row at a time.
2. For each row, try every column.
3. Skip a column if another queen shares the same column or diagonal.
4. When a row is filled, save the board and backtrack.
5. Remove the queen and try the next column.
6. Return all valid boards.
