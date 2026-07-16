# How We Solve Find And Replace in String

Validate each source against the original string, then rebuild left to right.

## Steps

1. For each `(index, source, target)`, record a hit if `s` matches at `index`.
2. Scan `s`; at a hit, append `target` and skip `len(source)`.
3. Otherwise copy the original character.
