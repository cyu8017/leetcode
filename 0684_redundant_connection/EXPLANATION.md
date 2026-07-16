# How We Solve Redundant Connection

Union-Find: the first edge whose ends share a parent closes the cycle.

## Steps

1. Process edges in order.
2. If `u` and `v` are already connected, that edge is redundant.
3. Otherwise unite their components.
