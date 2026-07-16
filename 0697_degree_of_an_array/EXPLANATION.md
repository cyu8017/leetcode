# How We Solve Degree of an Array

Degree is the max frequency; answer is the shortest span covering all occurrences of a degree value.

## Steps

1. Record first index, last index, and count per value.
2. Find the maximum frequency.
3. Among values with that frequency, take the minimum `last - first + 1`.
