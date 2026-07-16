# How We Solve Valid Number

Check if a string is a valid decimal number (with optional exponent).

## Steps

1. Scan the string one character at a time.
2. Track whether we have seen a digit, a dot, and an exponent.
3. Digits are always allowed; signs only after start or after e/E.
4. Only one dot, and no dot after an exponent.
5. Only one exponent, and it must come after at least one digit.
6. The string is valid only if it ends with at least one digit seen.
