# How We Solve Integer to Roman

Turn a number into Roman numerals (like 58 -> LVIII).

## Steps

1. Make a list of value + symbol pairs (biggest first).
2. Include subtractive pairs like 4 -> IV.
3. While number > 0, take the biggest symbol that fits.
4. Write that symbol and subtract its value.
5. Repeat until the number becomes zero.
6. Return the Roman string.
