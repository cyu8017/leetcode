# How We Solve Reconstruct Original Digits from English

English digit words share unique letters, so count digits in a fixed order that removes ambiguity.

## Steps

1. Count letters in the input string.
2. Read digits with unique markers first: zero, two, four, six, eight.
3. Derive remaining digits from leftover letters and output sorted digits.
