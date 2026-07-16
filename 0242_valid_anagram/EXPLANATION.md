# How We Solve Valid Anagram

Two strings are anagrams when every letter count matches.

## Steps

1. Reject different-length strings immediately.
2. Count letter frequencies for both strings in one pass.
3. Increment for characters in `s`.
4. Decrement for characters in `t`.
5. Return true only if all counts are zero.
