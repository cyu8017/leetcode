# How We Solve Binary Number with Alternating Bits

`n ^ (n >> 1)` is all ones iff bits alternate.

## Steps

1. XOR `n` with `n` shifted right by one.
2. Check that the result is a run of ones: `(x & (x + 1)) == 0`.
