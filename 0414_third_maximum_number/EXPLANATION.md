# How We Solve Third Maximum Number

Track the three largest distinct values in one pass.

## Steps

1. Skip duplicate values already seen in the top ranks.
2. Shift first, second, and third when a larger value appears.
3. Return third if it exists, otherwise the maximum.
