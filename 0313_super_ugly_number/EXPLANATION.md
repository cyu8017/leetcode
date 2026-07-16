# How We Solve Super Ugly Number

Multiple pointers generate the next super ugly number from given primes.

## Steps

1. Start with ugly list [1] and one pointer per prime.
2. Take the minimum candidate product each step.
3. Advance every pointer that produced that minimum.
