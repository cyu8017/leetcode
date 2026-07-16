# How We Solve Bricks Falling When Hit

Erase all hits first, union remaining roof-connected bricks, then undo hits in reverse.

## Steps

1. Clear hit cells and Union-Find bricks still attached to the top.
2. Re-add hits backward; measure the increase in roof component size.
3. Fallen count is `new_roof - old_roof - 1` (exclude the hit brick).
