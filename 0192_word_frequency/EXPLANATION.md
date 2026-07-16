# How We Solve Word Frequency

Use a Unix pipeline to split, count, and sort word frequencies.

## Steps

1. Read `words.txt` and squeeze spaces into newlines.
2. Sort the resulting words.
3. Count unique lines with `uniq -c`.
4. Sort those counts descending.
5. Print `word count` for each line.
