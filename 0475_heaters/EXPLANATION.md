# How We Solve Heaters

For each house, find the nearest heater with binary search on sorted heater positions.

## Steps

1. Sort heater coordinates.
2. For each house, locate insertion point with binary search.
3. Take the minimum distance to the closest heater on either side.
