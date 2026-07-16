# How We Solve Falling Squares

Simulate each square landing on the max height of overlapping prior intervals.

## Steps

1. Keep intervals `(left, right, height)` for placed squares.
2. For a new square, base height = max overlapping interval height (else 0).
3. Append the new max skyline height after each drop.
