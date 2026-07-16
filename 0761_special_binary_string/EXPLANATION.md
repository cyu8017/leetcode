# How We Solve Special Binary String

Special strings decompose as `1 + special + 0` chunks; sort those chunks descending.

## Steps

1. Split `s` into top-level special substrings by balance counting.
2. Recursively optimize each inner segment.
3. Sort the chunks lexicographically descending and concatenate.
