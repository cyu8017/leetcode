# How We Solve Minimize Max Distance to Gas Station

Binary search the max adjacent gap after placing `k` extra stations.

## Steps

1. Search distance `d` in `[0, stations[-1]-stations[0]]`.
2. Count stations needed so every gap ≤ `d`.
3. Shrink until the minimal feasible `d` (≈1e-6 precision).
