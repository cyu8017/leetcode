# How We Solve Super Washing Machines

Balance clothes evenly using prefix excess and per-machine surplus.

## Steps

1. Return `-1` if total clothes is not divisible by machine count.
2. Track running prefix imbalance while scanning machines.
3. Answer is max of absolute prefix load and any single-machine excess.
