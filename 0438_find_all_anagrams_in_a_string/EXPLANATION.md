# How We Solve Find All Anagrams in a String

Slide a fixed window of length `len(p)` and compare letter frequencies.

## Steps

1. Build the target frequency array for `p`.
2. Expand the window one character at a time in `s`.
3. When window size matches, record the start index if frequencies match.
