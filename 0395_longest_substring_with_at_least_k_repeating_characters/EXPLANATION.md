# How We Solve Longest Substring with At Least K Repeating Characters

Split on rare characters and recurse into valid segments.

## Steps

1. Count character frequencies in the current string.
2. If any character appears fewer than k times, split on it.
3. Recurse on each part and take the maximum length.
