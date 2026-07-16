# How We Solve Reshape the Matrix

Flatten row-major, then refill into the requested shape when sizes match.

## Steps

1. Reject reshape when `m * n != r * c` and return the original matrix.
2. Flatten all values in row-major order.
3. Chunk the flat list into `r` rows of length `c`.
