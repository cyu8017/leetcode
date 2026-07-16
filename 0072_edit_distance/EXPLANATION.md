# How We Solve Edit Distance

Find the fewest edits to turn one word into another.

## Steps

1. Build a table of costs for empty prefixes.
2. For each pair of characters, if they match, copy the diagonal cost.
3. If they differ, take 1 plus the minimum of delete, insert, or replace.
4. Use one row at a time to save space.
5. Return the bottom-right cost.
