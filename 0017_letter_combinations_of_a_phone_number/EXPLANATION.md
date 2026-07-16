# How We Solve Letter Combinations of a Phone Number

Phone keys map to letters (2->abc). Build all words from digits like "23".

## Steps

1. If digits are empty, return nothing.
2. Start with an empty word being built.
3. For each digit, try every letter on that key.
4. Add a letter, go to the next digit, then backtrack (remove letter).
5. When all digits are used, save the word.
6. Return all saved words.
