# How We Solve Couples Holding Hands

For each seat pair, swap so person `x` sits next to `x ^ 1`.

## Steps

1. Index every person’s current seat.
2. Walk couples of seats `(i, i+1)`.
3. If the partner is missing, swap them in and count one swap.
