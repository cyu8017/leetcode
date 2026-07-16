# How We Solve Prefix and Suffix Search

Index every `prefix#suffix` key to the latest word index.

## Steps

1. For each word, store all prefix/suffix combinations mapped to its index.
2. Later words overwrite earlier ones (largest index wins).
3. `f` looks up `pref#suff` or returns `-1`.
