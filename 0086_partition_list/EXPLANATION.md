# How We Solve Partition List

Reorder a list so values below x come before values x or larger.

## Steps

1. Make two lists: before and after.
2. Put each node into before if its value is less than x.
3. Otherwise put it into after.
4. Cut the after list and attach it after before.
5. Return the head of the before list.
