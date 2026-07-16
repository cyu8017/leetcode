# How We Solve Intersection of Two Arrays II

Frequency counts preserve duplicate intersections.

## Steps

1. Count occurrences in the first array.
2. Walk the second array and emit values with remaining count.
3. Decrement counts as matches are consumed.
