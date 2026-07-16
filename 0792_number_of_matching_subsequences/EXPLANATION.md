# How We Solve Number of Matching Subsequences

Bucket word iterators by their next needed character; advance through `s`.

## Steps

1. Group each word’s iterator under its first letter.
2. For each char in `s`, advance waiting iterators that need it.
3. Count words whose iterators are exhausted.
