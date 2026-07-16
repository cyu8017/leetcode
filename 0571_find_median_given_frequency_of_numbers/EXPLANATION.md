# How We Solve Find Median Given Frequency of Numbers

Use prefix frequency sums to locate the one or two middle values after decompression.

## Steps

1. Order numbers and compute running frequency totals.
2. Keep values whose compressed range covers the median index/indices.
3. Average those values and round to one decimal place.
