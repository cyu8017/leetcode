# How We Solve Find All Numbers Disappeared in an Array

Mark visited indices in place using negative signs, same idea as finding duplicates.

## Steps

1. For each value, negate the entry at index `abs(value) - 1`.
2. Indices that stay positive correspond to missing numbers `index + 1`.
3. Collect those indices into the result.
