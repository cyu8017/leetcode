# How We Solve K-th Smallest Prime Fraction

Min-heap of fractions `arr[i]/arr[j]` with decreasing denominators.

## Steps

1. Seed the heap with `arr[i]/arr[n-1]` for each numerator index.
2. Pop the smallest `k-1` times, pushing the next smaller denominator when possible.
3. The next pop is the kth fraction.
