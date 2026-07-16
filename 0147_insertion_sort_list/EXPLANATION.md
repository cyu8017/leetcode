# How We Solve Insertion Sort List

Insert each node into a growing sorted dummy-headed list.

## Steps

1. Create a dummy head for the sorted result.
2. Take nodes one by one from the input list.
3. Walk the sorted list until the insertion spot.
4. Splice the current node into place.
5. Return dummy.next when finished.
