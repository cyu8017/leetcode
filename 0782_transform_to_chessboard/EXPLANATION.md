# How We Solve Transform to Chessboard

A board is transformable iff every 2×2 has even parity; then count row/col swaps.

## Steps

1. Reject if any `board[0][0]^board[i][0]^board[0][j]^board[i][j]` is 1.
2. Check row/column ones counts are near `n/2`.
3. Compute minimal even swap counts for rows and columns; answer is half their sum.
