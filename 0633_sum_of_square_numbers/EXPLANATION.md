# How We Solve Sum of Square Numbers

Two-pointer search for `a^2 + b^2 = c` with `a` ascending and `b` descending.

## Steps

1. Set `left = 0` and `right = floor(sqrt(c))`.
2. Move inward according to whether the sum of squares is too small or too large.
3. Return true when an exact match is found.
