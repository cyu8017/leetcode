# How We Solve Combination Sum II

Pick numbers (each once) that add to target; no duplicate combos.

## Steps

1. Sort candidates so duplicates are together.
2. Backtrack like Combination Sum.
3. Skip using the same number twice at the same depth (duplicate skip rule).
4. Each number used at most once (next start is i+1).
5. Save paths that hit target exactly.
6. Return all unique combinations.
