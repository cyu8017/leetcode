# How We Solve Exam Room

Keep seated indices sorted; seat at the position maximizing min-distance.

## Steps

1. Empty room → seat `0`.
2. Consider left edge, right edge, and midpoints of gaps.
3. `leave` removes that index from the sorted list.
