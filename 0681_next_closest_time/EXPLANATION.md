# How We Solve Next Closest Time

Enumerate the next minutes on a 24h clock until all digits come from the input set.

## Steps

1. Collect the allowed digits from `HH:MM`.
2. Advance one minute at a time (wrapping midnight).
3. Return the first time whose digits are a subset of the allowed set.
