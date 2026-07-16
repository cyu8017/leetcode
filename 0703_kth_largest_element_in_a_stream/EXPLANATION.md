# How We Solve Kth Largest Element in a Stream

Keep a min-heap of size `k`; the root is the kth largest.

## Steps

1. Heapify the initial nums and shrink to size `k`.
2. On `add`, push the value and pop if the heap exceeds `k`.
3. Return the heap minimum.
