# How We Solve Next Greater Element II

Treat the circular array as doubled length with a decreasing monotonic stack.

## Steps

1. Scan indices `0 .. 2n-1`, using `index % n` for values.
2. Pop smaller stack tops when a larger element appears.
3. Leave `-1` where no greater element exists.
