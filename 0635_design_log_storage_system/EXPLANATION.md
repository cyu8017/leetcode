# How We Solve Design Log Storage System

Store logs and compare truncated timestamps according to the requested granularity.

## Steps

1. `put` appends `(id, timestamp)` pairs.
2. Map granularity to a prefix length (`Year`..`Second`).
3. `retrieve` returns ids whose truncated timestamps lie in `[start, end]`.
