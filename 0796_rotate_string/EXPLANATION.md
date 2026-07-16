# How We Solve Rotate String

`goal` is a rotation of `s` iff same length and `goal` is a substring of `s+s`.

## Steps

1. Reject unequal lengths.
2. Check membership of `goal` in `s+s`.
