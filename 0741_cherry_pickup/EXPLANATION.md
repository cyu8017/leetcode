# How We Solve Cherry Pickup

Simulate two people walking from `(0,0)` to `(n-1,n-1)` together so cherries aren’t double-counted.

## Steps

1. DP on positions `(r1,c1)` and `(r2,c2)` with `r2 = r1+c1-c2`.
2. Add cherries at both cells (once if they share a cell); skip thorns.
3. Take the best of the four move pairs; return `max(0, answer)`.
