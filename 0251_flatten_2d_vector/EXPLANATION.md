# How We Solve Flatten 2D Vector

Track the current row and column while skipping empty inner lists.

## Steps

1. Store the 2D vector and initialize row and column to 0.
2. Advance until the current position points to a valid element.
3. Return the current value and move the column forward.
4. Advance again after each read.
5. Report whether any elements remain.
