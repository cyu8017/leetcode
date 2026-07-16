# How We Solve Smallest Rotation with Highest Score

Difference array over rotation index `k` for when each `nums[i]` starts/stops scoring.

## Steps

1. Initialize score-change deltas; decrement at `(i - nums[i] + 1) % n`.
2. Prefix-sum the deltas to get scores for each `k`.
3. Return the smallest `k` with maximum score.
