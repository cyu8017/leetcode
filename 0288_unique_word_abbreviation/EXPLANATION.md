# How We Solve Unique Word Abbreviation

Group dictionary words by abbreviation and check uniqueness per key.

## Steps

1. Abbreviate each word as first char, middle length, last char (unchanged if length <= 2).
2. Map abbreviation keys to the set of full words.
3. A query word is unique if its key is unused or maps only to itself.
