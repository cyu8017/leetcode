# How We Solve Beautiful Arrangement

Backtracking counts permutations where index and value divide each other.

## Steps

1. Try placing unused numbers at the current position.
2. Allow the placement only if `i % num == 0` or `num % i == 0`.
3. Count complete permutations.
