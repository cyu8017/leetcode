# How We Solve Card Flipping Game

A value on both faces of the same card can never be good.

## Steps

1. Collect values that appear on both sides of one card.
2. Among all other face values, take the minimum.
3. Return `0` if none exist.
