# How We Solve Excel Sheet Column Number

Treat the title as a base-26 number with digits A-Z.

## Steps

1. Start the result at 0.
2. For each character left to right, multiply by 26.
3. Add the letter's 1-based value (`A` = 1).
4. Continue through the whole title.
5. Return the accumulated number.
