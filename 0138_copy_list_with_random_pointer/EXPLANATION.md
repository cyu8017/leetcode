# How We Solve Copy List with Random Pointer

Clone each node once, then copy both `next` and `random` through the map.

## Steps

1. Return null for an empty list.
2. Map each original node identity to its clone.
3. Create the clone before following pointers to handle cycles/shared refs.
4. Recursively (or iteratively) set `next` and `random` on the clone.
5. Return the clone of the head.
