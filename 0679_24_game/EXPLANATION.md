# How We Solve 24 Game

Backtrack over all ways to combine two numbers until one value remains.

## Steps

1. Pick every ordered pair, replace them with `+ - * /` results.
2. Recurse on the smaller list of floats.
3. Accept when the final value is within `1e-6` of 24.
