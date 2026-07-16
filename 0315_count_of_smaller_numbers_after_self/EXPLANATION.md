# How We Solve Count of Smaller Numbers After Self

Scan right to left and insert into a sorted list to count smaller elements.

## Steps

1. Process nums from end to start.
2. Binary search for insertion position in sorted list.
3. That position is the count of smaller numbers to the right.
