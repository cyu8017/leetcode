# How We Solve Generalized Abbreviation

Backtrack each position to either abbreviate or keep the character.

## Steps

1. At each index, extend the current run length count.
2. Or flush the count and append the literal character.
3. Collect all completed abbreviation strings.
