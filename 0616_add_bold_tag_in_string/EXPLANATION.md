# How We Solve Add Bold Tag in String

Mark every character covered by a word match, then wrap merged runs in `<b>` tags.

## Steps

1. For each word, find all occurrences and mark covered indices.
2. Scan the mark array and open/close bold tags around contiguous true runs.
3. Leave unmarked characters unchanged.
