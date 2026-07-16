# How We Solve Kth Smallest Number in Multiplication Table

Binary search the answer value; count how many table entries are ≤ mid.

## Steps

1. Search in `[1, m*n]`.
2. For mid `x`, count `min(x//row, n)` per row.
3. Shrink until the smallest `x` with count ≥ `k`.
