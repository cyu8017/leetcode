# How We Solve Queue Reconstruction by Height

Insert people from tallest to shortest at index k.

## Steps

1. Sort by height descending, then by k ascending.
2. Insert each person at position equal to their k value.
3. Earlier taller people already occupy the correct relative slots.
