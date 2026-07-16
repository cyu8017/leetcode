# How We Solve Sparse Matrix Multiplication

Skip zero entries when accumulating dot products.

## Steps

1. For each row of mat1, iterate only nonzero inner indices.
2. Multiply by nonzero entries in the matching row of mat2.
3. Accumulate into the result matrix.
