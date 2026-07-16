# How We Solve Meeting Rooms II

Sweep sorted start and end times to track concurrent meetings.

## Steps

1. Sort all start times and all end times separately.
2. Compare the earliest remaining start with the earliest end.
3. If a meeting starts before one ends, increase the room count.
4. Otherwise free a room by moving the end pointer.
5. Return the maximum rooms needed at once.
