# How We Solve Number of Islands II

Union-find tracks connected land components as cells are added.

## Steps

1. For each new land cell, create a new component.
2. Union with existing land neighbors and decrement count on merges.
3. Append the current island count after each add.
