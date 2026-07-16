# How We Solve Number of Lines To Write String

Fill lines of width 100 using each letter’s pixel width.

## Steps

1. Track current line width.
2. If the next letter won’t fit, start a new line.
3. Return `[lines, last_line_width]`.
