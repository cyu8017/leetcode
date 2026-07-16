# How We Solve Merge k Sorted Lists

Merge many sorted linked lists into one sorted list.

## Steps

1. Put the head of every non-empty list into a min-heap (smallest first).
2. Pop the smallest node and attach it to the answer.
3. If that node has a next, push the next into the heap.
4. Repeat until the heap is empty.
5. Return the merged list.
