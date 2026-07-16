# How We Solve Rectangle Overlap

Rectangles overlap iff they are not separated on any axis.

## Steps

1. Check right of one ≤ left of the other (and vice versa).
2. Same for top/bottom.
3. If none of the four separations hold, they overlap.
