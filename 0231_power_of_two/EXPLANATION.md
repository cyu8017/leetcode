# How We Solve Power of Two

A positive power of two has exactly one set bit.

## Steps

1. Reject non-positive numbers.
2. Compute `n & (n - 1)`.
3. Subtracting 1 clears the lowest set bit.
4. Powers of two become 0 after that operation.
5. Return whether the result is 0.
