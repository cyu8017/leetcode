# How We Solve Find All Duplicates in an Array

Use the array itself as a sign bit at each value's index.

## Steps

1. For each number, map to index `abs(num) - 1`.
2. If that slot is already negative, the number is a duplicate.
3. Otherwise negate the value at that index.
