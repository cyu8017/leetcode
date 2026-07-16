# How We Solve Word Pattern

Enforce a bijection between pattern characters and words.

## Steps

1. Split the string into words; reject length mismatches.
2. Map each character to a word and each word to a character.
3. Return false on any conflicting mapping.
4. Return true if every pair is consistent.
