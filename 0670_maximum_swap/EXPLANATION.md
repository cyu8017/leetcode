# How We Solve Maximum Swap

One swap: exchange the leftmost digit with a larger digit that appears later (prefer the largest, rightmost such).

## Steps

1. Record the last index of each digit 0–9.
2. Scan left to right; look for a larger digit to the right.
3. Swap once and return, or leave the number unchanged.
