# How We Solve Next Greater Element III

Compute the next permutation of the digits and reject 32-bit overflows.

## Steps

1. Find the rightmost ascent `digits[i] < digits[i + 1]`.
2. Swap with the smallest larger digit to its right, then reverse the suffix.
3. Return the value if it fits in a signed 32-bit int; otherwise `-1`.
