# How We Solve Nth Digit

Skip digit-length buckets until locating the exact digit.

## Steps

1. Subtract counts for 1-digit, 2-digit, ... ranges while n is large.
2. Find the number that contains the remaining digit.
3. Return that digit by its offset inside the number.
