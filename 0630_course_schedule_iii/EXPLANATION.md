# How We Solve Course Schedule III

Take courses by earliest deadline, dropping the longest one when a deadline is missed.

## Steps

1. Sort courses by `lastDay`.
2. Greedily take a course if it finishes on time; track durations in a max-heap.
3. If it overruns, replace the longest prior course when that improves the schedule.
