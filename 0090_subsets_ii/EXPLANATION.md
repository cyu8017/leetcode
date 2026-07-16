# How We Solve Subsets II

List unique subsets when the input may have duplicates.

## Steps

1. Sort the numbers so duplicates sit together.
2. Backtrack and always save the current path.
3. Skip a number if it equals the previous one at the same depth.
4. Choose a number, recurse, then undo the choice.
5. Return all unique subsets.
