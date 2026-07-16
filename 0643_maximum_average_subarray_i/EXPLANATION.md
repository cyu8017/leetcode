# How We Solve Maximum Average Subarray I

Slide a fixed window of length `k` and track the maximum sum.

## Steps

1. Sum the first `k` elements.
2. Slide the window by adding the next value and removing the oldest.
3. Return `max_sum / k`.
