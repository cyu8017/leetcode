# How We Solve Text Justification

Format words into lines of exact width with justified spacing.

## Steps

1. Greedily pack as many words as fit on each line.
2. If it is the last line or only one word, left-justify with spaces at the end.
3. Otherwise compute extra spaces to spread between words.
4. Give leftover spaces to the leftmost gaps first.
5. Build each line and repeat until all words are used.
