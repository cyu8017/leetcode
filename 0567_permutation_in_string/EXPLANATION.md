# How We Solve Permutation in String

A sliding window of length `|s1|` matches when character counts agree.

## Steps

1. Build the frequency map of `s1`.
2. Slide a window of the same length over `s2`.
3. Return true as soon as the window multiset equals `s1`.
