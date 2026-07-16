# How We Solve Design Phone Directory

Track available numbers in a set with deterministic minimum allocation.

## Steps

1. Initialize all slots as available.
2. get removes and returns the smallest available number.
3. check tests availability; release returns a number to the pool.
