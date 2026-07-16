# How We Solve Max Chunks To Make Sorted

For a permutation, a chunk can end when the max so far equals the index.

## Steps

1. Track the running maximum while scanning.
2. Whenever `max == i`, one more chunk is valid.
3. Return the chunk count.
