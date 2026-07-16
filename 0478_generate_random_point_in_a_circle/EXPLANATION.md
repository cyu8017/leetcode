# How We Solve Generate Random Point in a Circle

Rejection sampling inside the bounding square yields uniform points in the disk.

## Steps

1. Sample `(x, y)` uniformly in the square `[-r, r]`.
2. Reject pairs with `x^2 + y^2 > r^2`.
3. Translate accepted points by the circle center and round for output.
