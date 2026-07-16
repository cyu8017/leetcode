# How We Solve Smallest Rectangle Enclosing Black Pixels

Binary search each boundary using the known black pixel as a guide.

## Steps

1. Search left and right column bounds where black pixels exist.
2. Search top and bottom row bounds similarly.
3. Multiply width by height for the enclosing area.
