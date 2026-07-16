# How We Solve Delete Operation for Two Strings

Deletions needed equal total length minus twice the LCS length.

## Steps

1. Compute the longest common subsequence of the two words.
2. Characters in the LCS stay; everything else must be deleted.
3. Return `len(word1) + len(word2) - 2 * LCS`.
