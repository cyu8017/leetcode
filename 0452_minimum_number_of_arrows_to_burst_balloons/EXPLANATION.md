# How We Solve Minimum Number of Arrows to Burst Balloons

Greedy interval covering: sort balloons by end coordinate and shoot when the next start exceeds the current arrow position.

## Steps

1. Sort intervals by their right endpoint.
2. Place the first arrow at the first balloon's end.
3. Extend or add a new arrow whenever a balloon starts after the current arrow position.
