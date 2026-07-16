# How We Solve Rearrange String k Distance Apart

Greedy max-heap placement with a k-step cooldown queue.

## Steps

1. Reject impossible cases using the frequency bound.
2. Always place the most frequent available character next.
3. Requeue used characters after k positions have passed.
