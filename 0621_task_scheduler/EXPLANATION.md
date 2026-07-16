# How We Solve Task Scheduler

Idle time is driven by the most frequent task and the cooldown gap.

## Steps

1. Count task frequencies and find the maximum frequency `f`.
2. Count how many tasks share that maximum frequency.
3. Answer is `max(len(tasks), (f - 1) * (n + 1) + max_count)`.
