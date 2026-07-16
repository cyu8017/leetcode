# How We Solve Find Permutation

Build the lexicographically smallest permutation matching the I/D pattern with a stack.

## Steps

1. Push numbers sequentially onto a stack.
2. On `I`, pop the stack into the result (a decreasing run ends).
3. After scanning, pop any remaining stack values.
