# How We Solve Find Median from Data Stream

Two heaps keep the lower and upper halves balanced.

## Steps

1. Push each new number into the max-heap for the lower half.
2. Balance by moving the largest lower value to the min-heap upper half.
3. Rebalance sizes so lower has at least as many elements.
4. Return the top of lower or the average of both tops for the median.
