# How We Solve Find the Closest Palindrome

Generate a small candidate set from mirroring nearby prefixes, then pick the closest.

## Steps

1. Mirror `prefix - 1`, `prefix`, and `prefix + 1`.
2. Also consider `999…9` and `100…001` edge forms.
3. Drop `n` itself and choose the nearest value, breaking ties toward the smaller one.
