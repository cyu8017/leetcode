# How We Solve Largest Plus Sign

Precompute arm lengths in four directions; the plus order is the min arm at each cell.

## Steps

1. Mark mined cells as banned.
2. Sweep left/right/up/down to get consecutive ones from each side.
3. Take the minimum of the four arms; track the global max.
