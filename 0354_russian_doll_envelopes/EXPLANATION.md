# How We Solve Russian Doll Envelopes

Sort by width ascending and height descending, then LIS on heights.

## Steps

1. Sort envelopes to prevent equal-width nesting.
2. Build the longest increasing height subsequence.
3. Return the LIS length as the answer.
