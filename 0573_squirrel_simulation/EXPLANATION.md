# How We Solve Squirrel Simulation

Every nut must go to the tree twice except the first nut the squirrel picks up.

## Steps

1. Sum `2 * dist(tree, nut)` for all nuts.
2. Choose the first nut that maximizes `dist(tree, nut) - dist(squirrel, nut)`.
3. Subtract that savings from the total.
