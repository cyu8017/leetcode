# How We Solve Scramble String

Check if one string can be a scramble of another.

## Steps

1. Equal strings are scrambles; different letter counts are not.
2. Try every split of the string.
3. Check the no-swap case for both parts recursively.
4. Check the swap case for both parts recursively.
5. Memoize results so repeated pairs are not recomputed.
