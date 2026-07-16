# How We Solve Encode and Decode Strings

Prefix each string with its length and a delimiter before concatenation.

## Steps

1. For each string, write its length, a `#`, then the string bytes.
2. Join all encoded pieces into one string.
3. While decoding, read digits until `#` to get the length.
4. Slice the next length characters as one original string.
5. Repeat until the encoded string is exhausted.
