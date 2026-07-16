# How We Solve Remove Duplicate Letters

Monotonic stack builds the lexicographically smallest unique subsequence.

## Steps

1. Track last index of each character.
2. Pop larger stack tops while they appear later.
3. Append current char if not already used.
