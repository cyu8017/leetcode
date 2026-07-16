# How We Solve Daily Temperatures

Monotonic decreasing stack of indices waiting for a warmer day.

## Steps

1. For each day, pop cooler prior days and set their wait to the distance.
2. Push the current index.
3. Remaining stack indices stay `0`.
