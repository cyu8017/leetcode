# How We Solve Contains Duplicate III

Bucket numbers into width-sized groups inside a sliding window.

## Steps

1. Reject impossible inputs where the window or value tolerance is invalid.
2. Map each number to a bucket id using width `valueDiff + 1`.
3. If the same bucket already exists, the pair is close enough.
4. Also check the previous and next buckets for a valid neighbor.
5. Remove the bucket for the value leaving the window when it grows too large.
