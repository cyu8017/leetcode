# How We Solve 1-bit and 2-bit Characters

Scan from the left: `1` starts a two-bit char, `0` a one-bit char.

## Steps

1. Advance by 2 on `1`, by 1 on `0`, stopping before the last index.
2. The encoding is valid iff we land exactly on the final `0`.
