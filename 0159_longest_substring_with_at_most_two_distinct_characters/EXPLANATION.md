# How We Solve Longest Substring with At Most Two Distinct Characters

Sliding window with a frequency map limited to two distinct characters.

## Steps

1. Expand the right pointer and count characters.
2. While more than two distinct characters remain, shrink from the left.
3. Delete a character from the map when its count hits zero.
4. Track the maximum valid window length.
5. Return that length.
