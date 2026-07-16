# How We Solve One Edit Distance

Check whether one insert, delete, or replace turns `s` into `t`.

## Steps

1. Reject equal strings and length gaps larger than one.
2. Make `s` the shorter string when lengths differ.
3. Walk until the first mismatch.
4. For equal lengths, the suffixes after that index must match.
5. For insert/delete, `s` from the mismatch must equal `t` from the next char.
