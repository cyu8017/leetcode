# How We Solve Regular Expression Matching

Match a word to a pattern with `.` (any letter) and `*` (repeat).

## Steps

1. Make a table: word length x pattern length.
2. Empty word + empty pattern = match.
3. Fill each cell using smaller sub-problems.
4. `*` can mean "skip this pair" or "use another letter."
5. Matching letters copy the diagonal yes from smaller parts.
6. Bottom-right cell is the final answer.
