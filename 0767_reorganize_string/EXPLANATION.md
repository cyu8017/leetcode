# How We Solve Reorganize String

Greedily place the two currently most frequent remaining letters.

## Steps

1. Fail if any count exceeds `(n+1)//2`.
2. Use a max-heap of counts; repeatedly pop two letters and append them.
3. Push leftovers back until one letter remains.
