# How We Solve Design Circular Deque

Use a fixed ring buffer with a front index and a size counter.

## Steps

1. `insertFront` moves front backward; `insertLast` writes at front+size.
2. Deletes adjust front or size without shifting elements.
3. `getFront`/`getRear` read the ends when the deque is non-empty.
