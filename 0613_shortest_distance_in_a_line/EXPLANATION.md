# How We Solve Shortest Distance in a Line

The shortest gap on a line is the minimum absolute difference between distinct points.

## Steps

1. Self-join `Point` on `p1.x < p2.x`.
2. Take `MIN(ABS(p1.x - p2.x))`.
