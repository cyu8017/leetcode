# How We Solve Ambiguous Coordinates

Split the digit string into two parts; enumerate valid decimal placements.

## Steps

1. Remove the surrounding parentheses.
2. For each split point, generate legal numbers (no leading/trailing-zero issues).
3. Emit every `(left, right)` pair.
