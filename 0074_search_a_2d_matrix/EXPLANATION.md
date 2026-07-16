# How We Solve Search a 2D Matrix

Search a sorted matrix where each row and column is ordered.

## Steps

1. Start at the top-right corner.
2. If the cell equals the target, return true.
3. If the cell is bigger, move left.
4. If the cell is smaller, move down.
5. Stop when you leave the grid; return false.
