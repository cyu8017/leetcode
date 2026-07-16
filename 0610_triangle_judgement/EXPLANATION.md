# How We Solve Triangle Judgement

Three lengths form a triangle iff each pair sums to more than the third.

## Steps

1. For every row, test `x+y>z`, `x+z>y`, and `y+z>x`.
2. Emit `Yes` when all three hold, otherwise `No`.
