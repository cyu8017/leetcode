# How We Solve Pascal's Triangle

Build `numRows` rows where each entry is the sum of the two above it.

## Steps

1. Start with an empty list of rows.
2. For row `i`, place `1` at both ends.
3. Fill interior cells from the previous row's adjacent pair.
4. Append the finished row.
5. Return all rows.
