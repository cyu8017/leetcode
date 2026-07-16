# How We Solve Max Consecutive Ones

Track the longest run of consecutive 1s in one pass.

## Steps

1. Increment a counter on each 1 and update the best seen.
2. Reset the counter on 0.
3. Return the maximum run length.
