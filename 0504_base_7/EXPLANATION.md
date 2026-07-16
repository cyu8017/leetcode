# How We Solve Base 7

Repeatedly take remainders modulo 7 and build digits in reverse.

## Steps

1. Handle zero and remember the sign separately.
2. Collect `% 7` digits until the number becomes zero.
3. Reverse digits into the final string, restoring the sign.
