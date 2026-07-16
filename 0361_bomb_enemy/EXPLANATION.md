# How We Solve Bomb Enemy

Prefix counts of enemies along each row and column avoid repeated scans.

## Steps

1. Sweep each row left/right, counting enemies until a wall.
2. Sweep each column up/down the same way.
3. Place a bomb on empty cells and take the maximum hit total.
