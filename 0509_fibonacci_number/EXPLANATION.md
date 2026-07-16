# How We Solve Fibonacci Number

Iteratively advance two variables through the recurrence.

## Steps

1. Base cases: `F(0)=0`, `F(1)=1`.
2. Update `(prev, curr)` with `curr, prev+curr` for `n` steps.
3. Return the current value.
