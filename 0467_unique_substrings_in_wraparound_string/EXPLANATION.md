# How We Solve Unique Substrings in Wraparound String

Track the longest wraparound substring ending at each letter in the infinite `abc...z` string.

## Steps

1. Extend run length when consecutive letters differ by one modulo 26.
2. Reset length to one when the wraparound chain breaks.
3. Sum the best length per ending letter.
