# How We Solve Can Place Flowers

Greedily plant in every empty plot whose neighbors are also empty.

## Steps

1. Scan the flowerbed left to right.
2. Plant when the current plot and both neighbors are empty.
3. Stop early once `n` flowers have been placed.
