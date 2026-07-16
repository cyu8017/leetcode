# How We Solve Valid Perfect Square

Binary search finds whether any mid satisfies mid * mid == num.

## Steps

1. Search between 1 and num.
2. Compare square of mid with num.
3. Return true on exact match, false when search ends.
