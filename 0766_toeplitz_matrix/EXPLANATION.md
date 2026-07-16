# How We Solve Toeplitz Matrix

Every cell must equal the one immediately up-left on its diagonal.

## Steps

1. Scan cells with `r > 0` and `c > 0`.
2. Fail if `matrix[r][c] != matrix[r-1][c-1]`.
3. Otherwise the matrix is Toeplitz.
