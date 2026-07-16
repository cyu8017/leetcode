# How We Solve Two Sum III

Store frequencies so add is cheap and find checks complements.

## Steps

1. Keep a count map of inserted numbers.
2. On add, increment that number's count.
3. On find, scan each number for `value - number`.
4. If the complement equals the number, require count at least 2.
5. Otherwise succeed when the complement exists in the map.
