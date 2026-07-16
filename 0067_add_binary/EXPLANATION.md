# How We Solve Add Binary

Add two binary strings and return the sum as binary.

## Steps

1. Start from the rightmost bits of both strings.
2. Add the bits plus any carry.
3. Write the remainder (0 or 1) and update the carry.
4. Move left until both strings and carry are done.
5. Reverse the collected bits to get the answer.
