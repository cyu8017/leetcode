# How We Solve Race Car

BFS over `(position, speed)` with accelerate and reverse instructions.

## Steps

1. Start at position 0 with speed 1.
2. Branch: `A` → `(pos+speed, 2*speed)`, `R` → `(pos, ±1)`.
3. First time `pos == target` is the minimum instructions.
