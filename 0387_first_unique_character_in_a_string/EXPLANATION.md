# How We Solve First Unique Character in a String

Two-pass counting finds the earliest character with count one.

## Steps

1. Count every character in the string.
2. Scan left to right for the first count equal to 1.
3. Return -1 when no unique character exists.
