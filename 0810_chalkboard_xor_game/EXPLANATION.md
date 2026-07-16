# How We Solve Chalkboard XOR Game

Alice wins iff the total XOR is 0 or the length is even.

## Steps

1. Compute the XOR of all numbers.
2. If XOR is already 0, Alice wins immediately.
3. Otherwise she wins exactly when `n` is even.
