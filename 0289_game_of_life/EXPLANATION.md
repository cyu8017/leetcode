# How We Solve Game of Life

Encode next state in the second bit while scanning in one pass.

## Steps

1. Count live neighbors using the least significant bit of each cell.
2. Mark cells that should live next by setting bit 1 (value |= 2).
3. Shift every cell right by one bit to finalize the next generation.
