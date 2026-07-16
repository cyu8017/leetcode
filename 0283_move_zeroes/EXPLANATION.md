# How We Solve Move Zeroes

Compact non-zero values to the front, then fill the rest with zeros.

## Steps

1. Walk the array with a write pointer.
2. Copy each non-zero value to the write position and advance it.
3. Fill remaining slots from the write pointer to the end with zero.
