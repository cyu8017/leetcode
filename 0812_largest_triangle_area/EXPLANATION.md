# How We Solve Largest Triangle Area

Try every triple of points; area via the shoelace formula.

## Steps

1. Enumerate all combinations of 3 points.
2. Compute `abs(x1(y2-y3)+...)/2`.
3. Keep the maximum area.
