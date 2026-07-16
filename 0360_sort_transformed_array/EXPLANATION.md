# How We Solve Sort Transformed Array

Two pointers merge transformed values from both ends of sorted nums.

## Steps

1. Evaluate the quadratic at the left and right indices.
2. If a > 0, fill the result from the largest values inward.
3. If a < 0, fill from the smallest values outward.
