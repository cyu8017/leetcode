# How We Solve Different Ways to Add Parentheses

Split the expression at each operator and combine left and right results.

## Steps

1. If the expression is a single number, return it.
2. Scan for operators `+`, `-`, and `*`.
3. Recursively compute all values for the left and right subexpressions.
4. Combine each pair with the operator at the split point.
5. Return every possible result.
