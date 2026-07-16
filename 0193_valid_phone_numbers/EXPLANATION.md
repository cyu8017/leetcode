# How We Solve Valid Phone Numbers

Filter `file.txt` with a regex for the two allowed phone formats.

## Steps

1. Match `xxx-xxx-xxxx`.
2. Or match `(xxx) xxx-xxxx`.
3. Anchor the pattern to the whole line.
4. Use `grep -E` against `file.txt`.
5. Print only the valid numbers.
