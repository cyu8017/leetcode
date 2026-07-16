# How We Solve Combination Sum III

Backtrack over digits 1–9 to build k numbers that sum to n.

## Steps

1. Start with an empty path and search from digit 1.
2. Add each candidate digit if it does not exceed the remaining sum.
3. When the path length is k and the sum is 0, save a copy.
4. Always move to the next digit to avoid reuse.
5. Backtrack by removing the last chosen digit.
