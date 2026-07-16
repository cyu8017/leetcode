# How We Solve Perfect Squares

Breadth-first search finds the minimum number of square summands.

## Steps

1. Precompute all squares not greater than n.
2. BFS from n with steps equal to squares used so far.
3. Subtract each square and enqueue the remainder.
4. Return the step count when remainder reaches 0.
5. Skip already visited remainders.
