# How We Solve Excel Sheet Column Title

Convert the 1-indexed number to base-26 letters A-Z.

## Steps

1. Subtract one so the mapping is 0-based.
2. Take modulo 26 to get the next letter from the right.
3. Divide by 26 and repeat while the number remains.
4. Reverse the collected letters.
5. Return the title string.
