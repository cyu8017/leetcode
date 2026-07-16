# How We Solve Repeated Substring Pattern

If a string equals repeated copies of a substring, it appears inside its own rotation trick.

## Steps

1. Concatenate the string with itself.
2. Remove the first and last characters of the doubled string.
3. Check whether the original string occurs in that middle section.
