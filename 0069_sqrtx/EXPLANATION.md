# How We Solve Sqrt(x)

Find the integer square root (floor of √x).

## Steps

1. Handle small x (0 or 1) directly.
2. Binary search between 2 and x/2.
3. Compare mid×mid with x.
4. Move the search left or right.
5. Return the largest mid whose square is ≤ x.
