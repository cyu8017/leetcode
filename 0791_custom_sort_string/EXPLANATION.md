# How We Solve Custom Sort String

Emit characters in `order` first (by multiplicity), then any leftovers.

## Steps

1. Count characters in `s`.
2. Append each `order` character `count` times.
3. Append remaining characters in any order.
