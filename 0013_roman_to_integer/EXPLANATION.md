# How We Solve Roman to Integer

Turn Roman numerals back into a number.

## Steps

1. Start total = 0.
2. Read symbols from right to left.
3. If a symbol is smaller than the one before it, subtract it.
4. Otherwise add it.
5. Move left and repeat.
6. Return the total.
