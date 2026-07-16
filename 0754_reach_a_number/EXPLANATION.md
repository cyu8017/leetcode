# How We Solve Reach a Number

Take consecutive steps `1,2,3,…` until the sum reaches `target` with the same parity.

## Steps

1. Work with `|target|`.
2. Increase steps while `sum < target` or `sum-target` is odd.
3. Return the step count (flipping a step’s sign fixes odd excess).
