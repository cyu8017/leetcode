# How We Solve Reverse Bits

Build a 32-bit result by shifting in bits from the low end of `n`.

## Steps

1. Start the result at 0.
2. For each of 32 bits, shift result left.
3. Append the least significant bit of `n`.
4. Shift `n` right by one.
5. Return the reversed 32-bit integer.
