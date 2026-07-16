# How We Solve Shortest Word Distance III

When both words are the same, find the minimum gap between two occurrences.

## Steps

1. If word1 equals word2, track the previous occurrence index only.
2. Update the minimum distance whenever the same word appears again.
3. Otherwise use the standard two-index scan from problem 243.
4. Keep the smallest valid distance during one pass.
5. Return that distance.
