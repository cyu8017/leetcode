# How We Solve Island Perimeter

Each land cell contributes four edges, minus shared borders with neighbors above and left.

## Steps

1. Scan the grid for land cells (`1`).
2. Add four edges per land cell.
3. Subtract two for each adjacent land neighbor (top or left) to avoid double counting.
