# How We Solve Rotate Function

Use the recurrence relating successive rotations to update F in O(1).

## Steps

1. Compute the initial weighted sum and the total of all values.
2. Each rotation adds sum and subtracts n times the leaving element.
3. Track the maximum F across all rotations.
