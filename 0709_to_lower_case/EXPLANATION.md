# How We Solve To Lower Case

Map uppercase ASCII letters into lowercase by adding 32.

## Steps

1. For each character in `A..Z`, emit `chr(ord(ch)+32)`.
2. Leave all other characters unchanged.
3. Join into the result string.
