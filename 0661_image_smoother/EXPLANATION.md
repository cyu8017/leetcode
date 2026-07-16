# How We Solve Image Smoother

Replace each pixel with the floor average of its 3×3 neighborhood (or fewer on edges).

## Steps

1. For every cell, sum valid neighbors in the surrounding window.
2. Divide by the count of valid cells (integer division).
3. Write into a new matrix so originals stay intact.
