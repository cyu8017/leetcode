# How We Solve 3Sum

Find three numbers in a list that add to zero.

## Steps

1. Sort the list so duplicates sit together.
2. Pick a first number (i).
3. Use two fingers (left, right) on the rest to hunt for two more numbers.
4. If sum is zero, save the triple and skip duplicate values.
5. If sum is too small, move left up; if too big, move right down.
6. Return all unique triples.
