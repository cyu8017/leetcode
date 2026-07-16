# How We Solve Elimination Game

Track surviving interval endpoints instead of simulating every removal.

## Steps

1. Maintain left, right, step, and remaining count.
2. Move the active endpoint inward when elimination starts from that side.
3. Halve the interval each round until one number remains.
