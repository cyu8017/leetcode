# How We Solve Water and Jug Problem

Any reachable amount is a multiple of gcd(x, y) up to x + y.

## Steps

1. Reject targets above the combined capacity.
2. Accept target zero immediately.
3. Check target divisibility by gcd(x, y).
