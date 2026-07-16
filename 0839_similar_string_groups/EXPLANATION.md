# How We Solve Similar String Groups

Union-Find: connect strings that differ by a single swap (or are equal).

## Steps

1. Two strings are similar if they differ in 0 or exactly 2 swapped positions.
2. Union all similar pairs.
3. The number of components is the answer.
