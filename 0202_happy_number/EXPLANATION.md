# How We Solve Happy Number

Replace a number by the sum of squared digits and watch for 1 or a cycle.

## Steps

1. Compute the next value as the sum of each digit squared.
2. Record every value seen so far.
3. Stop with true when the value becomes 1.
4. Stop with false when a previously seen value reappears.
5. Return that boolean result.
