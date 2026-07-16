# How We Solve Non-negative Integers without Consecutive Ones

Digit DP on bits: precompute Fibonacci counts of valid bit strings by length.

## Steps

1. Let `fib[i]` be the number of valid strings of length `i`.
2. Walk `n`'s bits from high to low; when a `1` appears, add `fib[bit]`.
3. Stop early if two consecutive `1`s appear in `n`; otherwise include `n` itself.
