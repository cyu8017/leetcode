# How We Solve All O`one` Data Structure

Maintain a doubly linked list of count buckets plus a map from keys to their bucket.

## Steps

1. Each bucket stores all keys with the same frequency.
2. `inc` moves a key to the next higher bucket (creating it if needed).
3. `getMaxKey` / `getMinKey` read any key from the tail or head bucket.
