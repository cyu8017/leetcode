# How We Solve Remove K Digits

A monotonic increasing stack greedily drops peaks.

## Steps

1. Push digits while removing larger previous digits while removals remain.
2. Trim leftover removals from the end.
3. Strip leading zeros and return "0" if empty.
