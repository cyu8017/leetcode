# How We Solve Burst Balloons

Interval DP treats the last balloon burst in each range as the split point.

## Steps

1. Pad nums with 1 on both ends.
2. Fill DP for increasing interval lengths.
3. Try every last balloon in the range and maximize coins gained.
