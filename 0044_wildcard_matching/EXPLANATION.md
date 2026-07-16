# How We Solve Wildcard Matching

Does a pattern match a word? `?` = one any letter, `*` = any letters (even none).

## Steps

1. Build a yes/no table for every prefix of word vs pattern.
2. Empty word matches empty pattern.
3. A leading `*` can match empty at the start.
4. Fill the table: `*` can skip itself or eat another letter.
5. `?` or same letter copies the diagonal smaller yes.
6. Bottom-right cell is the final answer.
