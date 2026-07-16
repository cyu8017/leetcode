# How We Solve Add Two Numbers II

Push both lists onto stacks so digits can be added from least significant upward.

## Steps

1. Collect all digits from `l1` and `l2` into stacks.
2. Pop while either stack or carry remains, building the result list in reverse.
3. Prepend each new digit node to the answer list.
