# How We Solve Multiply Strings

Multiply big numbers given as strings (no built-in big math).

## Steps

1. If either number is "0", answer is "0".
2. Make an array big enough to hold all digit results.
3. Multiply each digit pair like on paper.
4. Add into the right slot and carry to the left slot.
5. Turn the array into a string and remove leading zeros.
6. Return the final string.
