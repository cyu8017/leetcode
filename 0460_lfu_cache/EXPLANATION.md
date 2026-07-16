# How We Solve LFU Cache

Track keys in frequency buckets and evict from the least frequently used bucket, breaking ties by LRU order within the bucket.

## Steps

1. Map each key to its value and frequency.
2. Keep lists of keys grouped by frequency, plus the current minimum frequency.
3. On get/put, promote keys to higher-frequency buckets; evict the oldest key in the min bucket when over capacity.
