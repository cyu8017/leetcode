# How We Solve First Bad Version

Binary search the first version that fails the bad check.

## Steps

1. Set the search range from 1 to n.
2. Test the middle version with `isBadVersion`.
3. If it is bad, search the left half including mid.
4. Otherwise search the right half after mid.
5. Return the left boundary when the range collapses.
