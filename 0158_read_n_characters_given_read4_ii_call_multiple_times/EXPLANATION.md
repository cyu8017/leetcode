# How We Solve Read N Characters Given read4 II

Persist leftover characters between calls so multiple reads share one file pointer.

## Steps

1. Keep an internal 4-char buffer with size and index.
2. For each query, drain leftovers before calling read4 again.
3. Refill the buffer only when it is empty.
4. Copy until the query count is met or the file ends.
5. Return the count for every query in order.
