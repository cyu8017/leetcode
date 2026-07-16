# How We Solve Optimal Division

Maximize `a/(b/c/...)` by putting the whole denominator in one group.

## Steps

1. One number: return it as a string.
2. Two numbers: return `a/b`.
3. Otherwise return `a/(b/c/.../z)` — the unique optimal grouping.
