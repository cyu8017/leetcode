# How We Solve Word Abbreviation

Increase prefix length until every abbreviation is unique and shorter than the original when possible.

## Steps

1. Build `prefix + middle + lastChar` with `middle = len(word) - prefix - 1`.
2. Group words sharing the same abbreviation.
3. Bump prefixes for conflicting groups until all abbreviations differ.
