# How We Solve Smallest Range Covering Elements from K Lists

Keep one pointer per list in a min-heap and advance the smallest value.

## Steps

1. Push the first element of every list and track the current maximum.
2. The heap min and current max form a candidate range.
3. Replace the min with the next value from its list until a list is exhausted.
