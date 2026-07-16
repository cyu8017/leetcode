# How We Solve Freedom Trail

DP over ring position and key index minimizes rotations plus presses.

## Steps

1. Precompute all ring indices for each character.
2. Recurse on `(ringIndex, keyIndex)` with memoization.
3. Add min clockwise/counter rotation plus one press at each step.
