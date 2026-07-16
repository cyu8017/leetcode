# How We Solve Erect the Fence

Build the convex hull with Andrew's monotone chain, keeping colinear boundary points.

## Steps

1. Sort points and build the lower hull with a strict right-turn pop.
2. Build the upper hull the same way on the reversed order.
3. Merge both chains and deduplicate endpoints.
