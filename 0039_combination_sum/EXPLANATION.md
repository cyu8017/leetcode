# How We Solve Combination Sum

Pick numbers (can reuse) that add to target.

## Steps

1. Sort candidates (optional but tidy).
2. Try building a path with backtracking.
3. If remaining target hits 0, save the path.
4. If remaining < 0, stop this branch.
5. For each candidate, add it and call again starting at same index (reuse allowed).
6. Backtrack by removing the last pick.
7. Return all combinations.
