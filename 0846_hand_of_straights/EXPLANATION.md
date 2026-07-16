# How We Solve Hand of Straights

Greedily form consecutive groups from the smallest remaining card.

## Steps

1. Fail early if `len(hand)` is not divisible by `groupSize`.
2. Count card frequencies.
3. Repeatedly take `groupSize` consecutive values starting at the smallest key.
