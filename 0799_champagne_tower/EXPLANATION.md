# How We Solve Champagne Tower

Simulate overflow row by row until the query row; each glass keeps at most 1.

## Steps

1. Pour all champagne into glass `(0,0)`.
2. Excess over 1 splits equally to the two glasses below.
3. Return `min(1, amount)` at `(query_row, query_glass)`.
