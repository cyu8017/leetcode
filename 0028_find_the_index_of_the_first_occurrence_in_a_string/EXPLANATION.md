# How We Solve Find the Index of the First Occurrence in a String

Find where a small word (needle) first appears inside a big word (haystack).

## Steps

1. If needle is empty, answer is 0.
2. Try every start position in haystack where needle could fit.
3. Compare needle letter by letter at that spot.
4. If all letters match, return that start index.
5. If none match, return -1.
