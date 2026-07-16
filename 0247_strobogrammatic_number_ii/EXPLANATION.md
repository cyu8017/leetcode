# How We Solve Strobogrammatic Number II

Recursively build every strobogrammatic number of length n.

## Steps

1. Base case: empty middle for even splits, or `0`, `1`, `8` for the center digit.
2. Try each valid outer digit pair.
3. Skip leading zero except when n is 1.
4. Recursively fill the inner substring.
5. Return all complete strings of length n.
