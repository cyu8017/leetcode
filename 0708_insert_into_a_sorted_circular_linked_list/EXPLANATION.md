# How We Solve Insert into a Sorted Circular Linked List

Walk until the insert fits between neighbors, including the wrap-around max→min edge.

## Steps

1. Empty list → single self-linked node.
2. Ensure the input is circular, then scan for `prev <= val <= curr` or the rotation point.
3. Splice the new node after `prev` and return the original head.
