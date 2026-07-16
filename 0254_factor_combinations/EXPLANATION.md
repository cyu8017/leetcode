# How We Solve Factor Combinations

Backtrack over factor splits and append the remaining value when valid.

## Steps

1. Try each factor starting from 2 up to the square root.
2. When a factor divides the remainder, push it and recurse.
3. After exploring smaller factors, append the remaining value if the path is non-empty.
4. Save combinations with at least two factors.
5. Backtrack and continue searching.
