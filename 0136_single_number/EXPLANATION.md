# How We Solve Single Number

XOR cancels every duplicated value and leaves the unique one.

## Steps

1. Start with 0.
2. XOR every number into the accumulator.
3. Pairs cancel to 0.
4. The leftover bits are the single number.
5. Return that value.
