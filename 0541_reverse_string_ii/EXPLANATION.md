# How We Solve Reverse String II

Reverse the first `k` characters of every `2k` block and leave the rest unchanged.

## Steps

1. Walk the string in steps of `2k`.
2. Reverse characters from the block start through `min(start + k, n)`.
3. Join the characters back into a string.
