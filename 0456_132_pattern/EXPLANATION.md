# How We Solve 132 Pattern

Scan from the right while tracking the best candidate for the middle value `3` in a `1-3-2` pattern.

## Steps

1. Maintain a stack of decreasing values as potential `3`s.
2. Track the largest valid middle value seen so far.
3. If a new value is smaller than that middle value, a `132` pattern exists.
