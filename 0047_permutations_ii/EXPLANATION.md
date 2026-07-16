# How We Solve Permutations II

Make all unique orders when the list can have duplicate numbers.

## Steps

1. Sort the list so duplicates sit together.
2. Use path + used[] backtracking like Permutations.
3. Skip a duplicate if the same number right before it is unused (same-level dup rule).
4. When path is full, save it.
5. Backtrack and try other choices.
6. Return all unique permutations.
