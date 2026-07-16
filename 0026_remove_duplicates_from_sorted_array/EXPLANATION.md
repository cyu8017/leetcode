# How We Solve Remove Duplicates from Sorted Array

Keep only unique numbers at the front of a sorted array.

## Steps

1. Use a write finger starting at 1 (index 0 stays).
2. Read each next number with a read finger.
3. If it is different from the last kept number, write it and move write forward.
4. Skip duplicates because the list is sorted.
5. Return how many unique numbers you kept.
