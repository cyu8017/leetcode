# How We Solve Minimum Time Difference

Times wrap around midnight, so compare both adjacent sorted times and the circular gap.

## Steps

1. Convert each `HH:MM` string to minutes since midnight.
2. Sort the minute values and take the minimum adjacent difference.
3. Also compare the wrap-around distance across the day boundary.
