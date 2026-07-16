# How We Solve Remove Duplicates from Sorted List II

Remove every value that appears more than once in a sorted list.

## Steps

1. Use a dummy node before the head.
2. Walk with previous and current pointers.
3. When current equals the next value, skip the whole duplicate group.
4. Otherwise advance previous.
5. Return the list after the dummy.
