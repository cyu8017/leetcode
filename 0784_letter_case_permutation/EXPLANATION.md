# How We Solve Letter Case Permutation

Expand each alphabetic character into lower/upper copies; digits stay fixed.

## Steps

1. Start with `[""]`.
2. For a letter, duplicate every prefix with both cases.
3. For a digit, append it to every prefix.
