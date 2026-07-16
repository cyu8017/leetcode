# How We Solve Range Module

Maintain a sorted list of disjoint half-open intervals `[left, right)`.

## Steps

1. `addRange` merges all overlapping intervals into one.
2. `removeRange` splits/trims intervals that intersect the cut.
3. `queryRange` checks whether one interval fully covers `[left, right)`.
