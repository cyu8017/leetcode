# How We Solve Partition Labels

Extend each partition to the farthest last occurrence of any character inside it.

## Steps

1. Record the last index of every character.
2. Scan left-to-right, growing `end` to those lasts.
3. When `i == end`, close a partition and start the next.
