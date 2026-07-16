# How We Solve Decode Ways

Count how many ways a digit string can map to letters A–Z.

## Steps

1. A leading zero cannot be decoded, so return 0.
2. Keep counts for the previous one and two positions.
3. A single non-zero digit can extend the previous count.
4. A valid two-digit number (10–26) can also extend the count before that.
5. Walk the string and return the final count.
