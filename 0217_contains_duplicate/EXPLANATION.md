# How We Solve Contains Duplicate

A duplicate exists exactly when some value appears more than once.

## Steps

1. Insert all numbers into a set.
2. Compare the set size with the array length.
3. If the set is smaller, at least one duplicate exists.
4. Otherwise every value is unique.
5. Return the comparison result.
