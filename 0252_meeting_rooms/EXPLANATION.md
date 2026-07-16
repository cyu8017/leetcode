# How We Solve Meeting Rooms

Sort meetings by start time and check for overlap.

## Steps

1. Sort intervals by their start times.
2. Walk through consecutive meetings.
3. If the next meeting starts before the previous one ends, return false.
4. Otherwise continue scanning.
5. Return true when no overlap exists.
