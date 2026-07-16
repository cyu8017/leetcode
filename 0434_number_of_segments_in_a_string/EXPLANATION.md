# How We Solve Number of Segments in a String

Count contiguous non-space runs in one pass.

## Steps

1. Track whether the current character is inside a segment.
2. Increment the count when a non-space character starts a new segment.
3. Reset the flag on spaces.
