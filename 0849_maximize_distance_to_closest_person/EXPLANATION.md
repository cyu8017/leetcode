# How We Solve Maximize Distance to Closest Person

Seat at an edge or in the middle of the widest empty gap.

## Steps

1. Track gaps between occupied seats.
2. Mid-gap distance is `gap // 2`; edges use the full run of zeros.
3. Return the maximum of those distances.
