# How We Solve Rectangle Area

Add both rectangle areas and subtract their overlap.

## Steps

1. Compute the area of rectangle A.
2. Compute the area of rectangle B.
3. Find overlap width as the horizontal intersection length.
4. Find overlap height as the vertical intersection length.
5. Return `areaA + areaB - overlapWidth * overlapHeight`.
