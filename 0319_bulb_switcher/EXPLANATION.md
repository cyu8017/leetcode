# How We Solve Bulb Switcher

Only perfect-square positions remain on after n toggles.

## Steps

1. Observe each bulb toggles once per divisor.
2. Bulbs end on when toggled an odd number of times.
3. Return floor(sqrt(n)).
