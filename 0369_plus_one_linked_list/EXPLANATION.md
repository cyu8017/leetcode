# How We Solve Plus One Linked List

Carry only affects the suffix after the rightmost non-nine digit.

## Steps

1. Walk the list, remembering the last node not equal to 9.
2. Increment that node and zero all following nodes.
3. Use a sentinel when the carry creates a new leading digit.
