# How We Solve Set Intersection Size At Least Two

Greedy: sort by end point; always cover with the rightmost needed points.

## Steps

1. Sort intervals by ascending end (then start).
2. Keep the two largest chosen points so far.
3. Add one or two new right-end points when an interval is under-covered.
