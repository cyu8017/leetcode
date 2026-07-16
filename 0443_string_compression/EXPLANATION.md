# How We Solve String Compression

Compress runs in place with read/write pointers.

## Steps

1. Scan each group of identical characters.
2. Write the character, then write count digits when count exceeds one.
3. Return the new compressed length.
