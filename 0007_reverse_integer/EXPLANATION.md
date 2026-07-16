# How We Solve Reverse Integer

Flip the digits (123 becomes 321).

## Steps

1. Start with reversed = 0.
2. Peel off the last digit of the number.
3. Stick it on the end of reversed.
4. Remove that digit from the original number.
5. Stop if the answer gets too big (32-bit limit).
6. Return reversed, or 0 if overflow.
