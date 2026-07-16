# How We Solve Largest Rectangle in Histogram

Find the largest rectangle area under a histogram.

## Steps

1. Use a monotonic stack of rising bar indexes.
2. Add a zero-height bar at the end as a stopper.
3. When the current bar is shorter, pop taller bars.
4. For each pop, width is the span to the new stack top.
5. Track the maximum height × width.
