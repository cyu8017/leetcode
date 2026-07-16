# How We Solve H-Index II

Binary search the smallest index whose citation count satisfies h.

## Steps

1. Binary search over the sorted citation array.
2. For a mid index, compute how many papers remain at or after it.
3. If citations[mid] is at least that count, search left.
4. Otherwise search right.
5. Return n minus the final left boundary.
