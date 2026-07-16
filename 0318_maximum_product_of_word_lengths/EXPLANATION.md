# How We Solve Maximum Product of Word Lengths

Bitmask each word and maximize product when masks do not overlap.

## Steps

1. Build a bitmask for each word without duplicate letters.
2. Compare pairs with no shared bits.
3. Track the maximum length product.
