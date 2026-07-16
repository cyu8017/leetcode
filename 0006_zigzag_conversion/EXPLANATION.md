# How We Solve Zigzag Conversion

Write letters in a zigzag, then read row by row.

## Steps

1. Make one row bucket for each zigzag level.
2. Walk through each letter.
3. Put the letter in the current row.
4. Bounce down then up between rows.
5. Glue all rows together left to right.
6. Return the final string.
