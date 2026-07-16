# How We Solve IPO

Repeatedly take the most profitable affordable project using a max-heap.

## Steps

1. Sort projects by required capital.
2. Push all newly affordable profits into a max-heap.
3. Pop the best profit up to k times and add it to current capital.
