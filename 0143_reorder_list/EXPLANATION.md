# How We Solve Reorder List

Split, reverse the second half, then weave the two halves together.

## Steps

1. Find the midpoint with slow/fast pointers.
2. Cut the list into first and second halves.
3. Reverse the second half in place.
4. Alternate nodes from the first half and the reversed second half.
5. The list is updated in place.
