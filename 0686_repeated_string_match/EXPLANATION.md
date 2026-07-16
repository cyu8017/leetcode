# How We Solve Repeated String Match

Repeat `a` enough times to cover `b`, then check one more copy if needed.

## Steps

1. Let `repeats = ceil(len(b) / len(a))`.
2. If `b` is in `a * repeats`, return that count.
3. Else try one extra repeat; otherwise `-1`.
