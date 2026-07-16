# How We Solve Find the Difference

XOR cancels matching characters and leaves the extra one.

## Steps

1. XOR every character code in s and t together.
2. The remaining value is the added character's code.
3. Convert that code back to a one-character string.
