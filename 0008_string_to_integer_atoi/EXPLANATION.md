# How We Solve String to Integer (atoi)

Turn text like "   -42abc" into the number -42.

## Steps

1. Skip spaces at the start.
2. Read + or - if there is one.
3. Read digits while they are 0-9.
4. Stop at the first non-digit.
5. Clamp to 32-bit min/max if needed.
6. Return the integer.
