# How We Solve IP to CIDR

Greedily cover the next `n` addresses with the largest aligned CIDR block each time.

## Steps

1. Convert the start IP to an integer.
2. The block size is limited by trailing zeros (alignment) and remaining `n`.
3. Emit `ip/mask`, advance, and repeat until `n` is covered.
