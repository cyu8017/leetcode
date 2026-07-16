# How We Solve Sort List

Merge-sort the linked list in O(n log n) time and O(1) extra pointer space.

## Steps

1. Base case: empty or single-node lists are already sorted.
2. Split at the midpoint with slow/fast pointers.
3. Recursively sort both halves.
4. Merge the two sorted halves by value.
5. Return the merged head.
