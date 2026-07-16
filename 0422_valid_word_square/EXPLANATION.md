# How We Solve Valid Word Square

A word square is valid when character at `(row, col)` equals character at `(col, row)` for every filled cell.

## Steps

1. Walk each row and column index within the current word.
2. Reject if the mirrored position is out of bounds.
3. Reject on any character mismatch; otherwise the square is valid.
