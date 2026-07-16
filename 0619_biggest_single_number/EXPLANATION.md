# How We Solve Biggest Single Number

Keep numbers that appear once, then take the maximum (or null).

## Steps

1. Group `MyNumbers` by `num` with `HAVING COUNT(*) = 1`.
2. Select `MAX(num)` from that set.
