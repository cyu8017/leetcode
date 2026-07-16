# How We Solve Insert Interval

Add a new time range into a sorted list and merge overlaps.

## Steps

1. Copy all intervals that end before the new one starts.
2. Merge every interval that overlaps the new one.
3. Add the merged new interval once.
4. Copy all remaining intervals that start after it.
5. Return the updated list.
