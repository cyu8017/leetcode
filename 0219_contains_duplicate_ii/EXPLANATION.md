# How We Solve Contains Duplicate II

Track the most recent index of each value while scanning the array.

## Steps

1. Walk through the array left to right.
2. Store each value's latest index in a hash map.
3. If the value was seen before, check the index gap.
4. Return true when the gap is at most k.
5. Otherwise update the stored index and continue.
