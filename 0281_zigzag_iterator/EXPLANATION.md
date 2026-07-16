# How We Solve Zigzag Iterator

Alternate between two vectors, skipping exhausted lists.

## Steps

1. Track an index and turn for each vector.
2. On `next`, advance the current vector and flip the turn.
3. Skip vectors that are already exhausted.
4. `hasNext` is true while any vector has remaining elements.
