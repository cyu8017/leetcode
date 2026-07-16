# How We Solve Palindrome Pairs

Split each word and pair with reverse halves found in a hash map.

## Steps

1. For every split, test whether the left or right part is a palindrome.
2. Look up the reverse of the other part in the word index.
3. Store pairs in a set to avoid duplicates.
