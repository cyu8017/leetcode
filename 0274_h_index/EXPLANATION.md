# How We Solve H-Index

Bucket counts by citation frequency to find the largest valid h.

## Steps

1. Place each citation into a bucket capped at n.
2. Walk buckets from high to low while accumulating paper counts.
3. When the accumulated count reaches the bucket index, that h works.
4. Return the largest such h.
