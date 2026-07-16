# How We Solve Merge Two Sorted Lists

Merge two sorted linked lists into one sorted list.

## Steps

1. Make a dummy head for the answer list.
2. Compare the front nodes of both lists.
3. Attach the smaller node to the answer and move that list forward.
4. Repeat until one list is empty.
5. Attach the rest of the non-empty list.
6. Return the merged list after dummy.
