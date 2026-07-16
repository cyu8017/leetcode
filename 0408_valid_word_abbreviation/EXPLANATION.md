# How We Solve Valid Word Abbreviation

Two pointers expand numeric skips and match literal characters.

## Steps

1. Reject leading zeros in number segments.
2. Advance through the word by the parsed count.
3. Require both pointers to finish exactly.
