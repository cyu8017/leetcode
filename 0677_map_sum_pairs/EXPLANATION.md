# How We Solve Map Sum Pairs

Keep key values and maintain running sums for every prefix.

## Steps

1. On insert, compute the delta versus any previous value for that key.
2. Add the delta to every prefix of the key.
3. `sum(prefix)` reads the maintained prefix total.
