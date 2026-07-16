# How We Solve Reaching Points

Work backward from `(tx, ty)` with modulo, since forward branches explode.

## Steps

1. While above `(sx, sy)`, reduce the larger coordinate modulo the smaller.
2. When one coordinate matches the start, check the other via divisibility.
3. Succeed only if both coordinates land on the start.
