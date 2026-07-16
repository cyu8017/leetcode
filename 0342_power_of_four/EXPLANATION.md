# How We Solve Power of Four

A power of four is a power of two whose single bit sits at an odd index.

## Steps

1. Reject non-positive values.
2. Check exactly one set bit with n & (n - 1) == 0.
3. Confirm n % 3 == 1, which holds for powers of four.
