# How We Solve Range Sum Query 2D Mutable

A 2D Fenwick tree handles cell updates and rectangle sums.

## Steps

1. Build the 2D BIT from the matrix.
2. Update one cell by adding its delta through nested loops.
3. Query a rectangle with four 2D prefix sums.
