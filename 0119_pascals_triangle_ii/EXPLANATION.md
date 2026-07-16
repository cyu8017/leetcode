# How We Solve Pascal's Triangle II

Return only the 0-indexed row, updating one array in place.

## Steps

1. Start with `[1]`.
2. For each next row index, append a trailing `1`.
3. Update interior cells right-to-left so older values stay available.
4. Each update adds the previous cell into the current cell.
5. Return the finished row.
