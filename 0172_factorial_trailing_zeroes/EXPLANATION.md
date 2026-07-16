# How We Solve Factorial Trailing Zeroes

Count factors of 5 in `n!`; each contributes a trailing zero.

## Steps

1. Initialize a counter to 0.
2. Divide `n` by 5 and add the quotient.
3. Repeat with the new quotient.
4. Stop when the quotient becomes 0.
5. Return the total count of fives.
