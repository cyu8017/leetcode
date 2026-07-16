# How We Solve Array Nesting

The array is a functional graph of cycles; the answer is the longest cycle.

## Steps

1. From each unvisited index, follow `i -> nums[i]` until a cycle closes.
2. Mark visited indices while walking so each cycle is measured once.
3. Keep the maximum cycle length.
