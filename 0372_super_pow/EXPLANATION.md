# How We Solve Super Pow

Process exponent digits left to right with modular exponentiation.

## Steps

1. Reduce a modulo 1337.
2. For each digit, raise current result to the 10th power mod 1337.
3. Multiply by a to the digit power mod 1337.
