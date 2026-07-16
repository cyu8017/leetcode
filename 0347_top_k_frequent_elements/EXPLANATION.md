# How We Solve Top K Frequent Elements

Bucket sort groups values by frequency for linear-time extraction.

## Steps

1. Count frequencies with a hash map.
2. Place values into buckets indexed by count.
3. Scan buckets from highest count until k elements are collected.
