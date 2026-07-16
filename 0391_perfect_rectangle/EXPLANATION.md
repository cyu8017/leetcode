# How We Solve Perfect Rectangle

Corner XOR and area equality prove a perfect cover without gaps or overlaps.

## Steps

1. Track each rectangle corner in a set, toggling membership on repeats.
2. Accumulate total area and the bounding box extents.
3. Accept only when four outer corners remain and areas match.
