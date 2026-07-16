# How We Solve Convert a Number to Hexadecimal

Treat the value as unsigned and emit nibbles from least significant.

## Steps

1. Mask to 32 bits so negatives use two's complement.
2. Append hex digits for the low 4 bits repeatedly.
3. Reverse the collected digits into the final string.
