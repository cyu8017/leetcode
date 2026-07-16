# How We Solve Human Traffic of Stadium

Group busy days by consecutive ids, then keep groups of length ≥ 3.

## Steps

1. Filter rows with `people >= 100`.
2. Assign a group key with `id - row_number()`.
3. Keep groups that have at least three rows and order by `visit_date`.
