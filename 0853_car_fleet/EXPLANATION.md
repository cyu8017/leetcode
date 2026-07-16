# How We Solve Car Fleet

Sort cars by position from the destination; count time-to-target fleets.

## Steps

1. Sort by position descending (closest to target first).
2. Compute arrival time for each car.
3. A new fleet forms only when time exceeds the slowest fleet ahead.
