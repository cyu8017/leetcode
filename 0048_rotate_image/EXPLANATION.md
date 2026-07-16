# How We Solve Rotate Image

Turn a square grid 90 degrees clockwise **in place**.

## Steps

1. Transpose: swap matrix[i][j] with matrix[j][i] for i < j.
2. Reverse each row left to right.
3. The matrix is now rotated 90° clockwise.
