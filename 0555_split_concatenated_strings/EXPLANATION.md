# How We Solve Split Concatenated Strings

Orient each string for max lex order, then try every cut on every string.

## Steps

1. For middle strings, keep `max(s, reverse(s))`.
2. For each string as the cut host, try both orientations and every start index.
3. Track the lexicographically largest formed loop string.
