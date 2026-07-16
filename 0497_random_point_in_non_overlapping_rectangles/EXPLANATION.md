# How We Solve Random Point in Non-overlapping Rectangles

Pick a uniform random integer point using prefix sums over rectangle areas.

## Steps

1. Build cumulative counts of points per rectangle.
2. Choose a global linear index with randomness (mocked in tests).
3. Decode index to `(x, y)` inside the chosen rectangle.
