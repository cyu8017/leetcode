# How We Solve Preimage Size of Factorial Zeroes Function

`zeta(n)` (trailing zeros) jumps over some values; hits come in blocks of 5.

## Steps

1. Binary-search the smallest `n` with `zeta(n) >= k`.
2. If `zeta(n) == k`, there are exactly 5 such `n`; else 0.
