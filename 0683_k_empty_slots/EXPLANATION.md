# How We Solve K Empty Slots

Map each position to its bloom day; slide windows of length `k+2`.

## Steps

1. Build `days[pos]` = day that bulb blooms.
2. For window `[left, left+k+1]`, require every middle day later than both ends.
3. Track the earliest valid `max(end days)`; jump left on violations.
