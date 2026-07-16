# How We Solve Number Of Corner Rectangles

For every pair of rows, count shared `1`-columns; each pair of those columns forms a rectangle.

## Steps

1. Enumerate row pairs `(i, j)`.
2. Count columns where both rows have a `1`.
3. Add `C(count, 2)` to the answer.
