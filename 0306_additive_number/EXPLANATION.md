# How We Solve Additive Number

Try every split for the first two numbers, then verify the additive chain.

## Steps

1. Enumerate first and second substrings with leading-zero checks.
2. While digits remain, require the next chunk to equal their sum.
3. Return true if the entire string is consumed.
