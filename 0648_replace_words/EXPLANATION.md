# How We Solve Replace Words

Replace each word with the shortest dictionary root that is a prefix.

## Steps

1. Put all roots into a set.
2. For each sentence word, try prefixes from shortest to longest.
3. Swap in the first matching root, otherwise keep the word.
