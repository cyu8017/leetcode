# How We Solve Candy Crush

Repeatedly crush runs of 3+ equal candies, then drop gravity until stable.

## Steps

1. Mark horizontal/vertical runs of length ≥ 3 (via negative tags).
2. Collapse each column downward, filling zeros above.
3. Repeat until a pass finds nothing to crush.
