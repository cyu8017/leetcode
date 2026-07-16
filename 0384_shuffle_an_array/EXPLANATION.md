# How We Solve Shuffle an Array

Keep the original array and Fisher-Yates shuffle a fresh copy each time.

## Steps

1. Store the initial nums in reset state.
2. reset returns a copy of the original array.
3. shuffle copies original values and applies random permutation.
