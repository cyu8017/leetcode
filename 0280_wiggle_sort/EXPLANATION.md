# How We Solve Wiggle Sort

Swap adjacent elements when the current parity violates the wiggle rule.

## Steps

1. Walk from index 1 to the end.
2. On odd indices, ensure the value is greater than its left neighbor.
3. On even indices, ensure the value is less than its left neighbor.
4. Swap with the left neighbor when a rule is broken.
5. Continue until the array satisfies the wiggle pattern.
