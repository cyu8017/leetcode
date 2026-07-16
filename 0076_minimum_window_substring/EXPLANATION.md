# How We Solve Minimum Window Substring

Find the smallest substring of s that contains all letters of t.

## Steps

1. Count how many of each letter t needs.
2. Expand the window right, updating counts.
3. When all needed letters are satisfied, try shrinking from the left.
4. Save the smallest valid window seen.
5. Return that substring, or empty if none exists.
