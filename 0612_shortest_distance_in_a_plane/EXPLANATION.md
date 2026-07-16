# How We Solve Shortest Distance in a Plane

Compute Euclidean distance for every unordered point pair and take the minimum.

## Steps

1. Self-join `Point2D` so each pair is considered once.
2. Evaluate `sqrt((x2-x1)^2 + (y2-y1)^2)`.
3. Round the minimum to two decimals.
