# How We Solve Binary Watch

Enumerate valid hour/minute pairs whose LED bit counts sum to turnedOn.

## Steps

1. Loop hours 0-11 and minutes 0-59.
2. Count set bits in both values.
3. Format matching times as H:MM.
