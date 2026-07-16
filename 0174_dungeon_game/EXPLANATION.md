# How We Solve Dungeon Game

DP backward from the princess: each cell stores the min HP needed there.

## Steps

1. Work from the bottom-right corner toward the start.
2. Need enough HP so that after the room's effect you can still reach the exit.
3. Take the cheaper of the right and down options.
4. Clamp any non-positive need up to 1.
5. The top-left DP value is the answer.
