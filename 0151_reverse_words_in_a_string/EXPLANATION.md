# How We Solve Reverse Words in a String

Split on whitespace, reverse the word list, and join with single spaces.

## Steps

1. Split the string on any run of whitespace.
2. Drop empty tokens created by leading or trailing spaces.
3. Reverse the remaining words.
4. Join them with a single space.
5. Return the rebuilt string.
