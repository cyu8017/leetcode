# How We Solve My Calendar I

Store booked half-open intervals; reject any overlap.

## Steps

1. On `book(start, end)`, scan existing intervals.
2. Overlap if `start < otherEnd` and `otherStart < end`.
3. Append and return true when clear.
