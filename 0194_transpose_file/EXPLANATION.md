# How We Solve Transpose File

Use `awk` to collect each column into a row while reading the file.

## Steps

1. For every field index, append the current token to that column buffer.
2. Separate later tokens with spaces.
3. After the file ends, print each column buffer as a line.
4. Preserve the original left-to-right field order.
5. Return the transposed text.
