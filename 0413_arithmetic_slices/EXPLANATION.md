# How We Solve Arithmetic Slices

Extend each arithmetic run and count new ending slices.

## Steps

1. Compare consecutive differences starting at index 2.
2. Increment the current run length when the difference matches.
3. Add the run length to the total count.
