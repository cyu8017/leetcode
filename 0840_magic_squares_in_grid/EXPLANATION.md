# How We Solve Magic Squares In Grid

Check every `3×3` window for digits `1..9` unique and magic sum `15`.

## Steps

1. Slide a `3×3` over the grid.
2. Require distinct values `1` through `9`.
3. Verify all rows, columns, and both diagonals sum to `15`.
