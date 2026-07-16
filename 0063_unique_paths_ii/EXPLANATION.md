# How We Solve Unique Paths II

Count paths on a grid with blocked cells.

## Steps

1. If the start cell is blocked, return 0.
2. Keep one row of path counts, starting with 1 at the top-left.
3. For each row, zero out blocked cells.
4. For open cells, add the count from the left (same row update).
5. Also zero the first column when that row's start is blocked.
6. Return the bottom-right count.
