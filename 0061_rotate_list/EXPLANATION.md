# How We Solve Rotate List

Move the last k nodes of a linked list to the front.

## Steps

1. If the list is empty or has one node, return it.
2. Find the tail and count the list length.
3. Connect the tail to the head to form a circle.
4. Reduce k using k mod length.
5. Walk length − k steps to find the new tail.
6. Break the circle after the new tail and return the new head.
