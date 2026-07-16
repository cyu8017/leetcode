# How We Solve Construct Quad Tree

Recursively split the grid into four quadrants and merge uniform regions into leaf nodes.

## Steps

1. Base case: a 1x1 cell becomes a leaf with that value.
2. Build the four child quadrants recursively.
3. If all four children are leaves with the same value, return one merged leaf.
4. Otherwise return an internal node pointing to the four children.
