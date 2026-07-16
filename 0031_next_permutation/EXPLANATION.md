# How We Solve Next Permutation

Rearrange numbers into the **next bigger** order (like 123 -> 132).

## Steps

1. Find the rightmost place where a number is smaller than its neighbor to the right.
2. If none, reverse the whole list (wrap to smallest order).
3. Find the smallest number to the right that is bigger than that place.
4. Swap them.
5. Reverse everything after that place to get the smallest tail.
6. The array is now the next permutation.
