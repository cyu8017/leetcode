# How We Solve Maximum Distance in Arrays

Track the global min and max seen so far while scanning arrays one by one.

## Steps

1. Initialize min/max from the first array.
2. For each later array, try pairing its ends against the running min/max.
3. Then update the running min/max with the current array's ends.
