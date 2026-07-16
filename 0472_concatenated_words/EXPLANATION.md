# How We Solve Concatenated Words

Process words from shortest to longest and test whether each word can be built from smaller dictionary words.

## Steps

1. Sort words by length so building blocks are available first.
2. Temporarily remove the current word from the dictionary.
3. Run word-break DP to see if the word decomposes into dictionary entries.
