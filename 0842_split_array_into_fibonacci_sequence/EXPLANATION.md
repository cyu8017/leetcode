# How We Solve Split Array into Fibonacci Sequence

Backtrack over splits that keep a valid Fibonacci recurrence.

## Steps

1. Grow the next number from the remaining digit string.
2. Reject leading zeros and values outside 32-bit ints.
3. Accept the first split with length ≥ 3 that consumes the whole string.
