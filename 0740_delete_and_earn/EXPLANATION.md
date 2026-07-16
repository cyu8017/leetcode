# How We Solve Delete and Earn

Bucket points by value; then house-robber DP over adjacent numbers.

## Steps

1. `points[v]` = `v * count(v)`.
2. Taking `v` forbids `v-1` and `v+1`.
3. Run take/skip DP across values `0..max(nums)`.
