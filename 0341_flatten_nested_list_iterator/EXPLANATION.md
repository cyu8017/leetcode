# How We Solve Flatten Nested List Iterator

A stack lazily expands nested lists when the next integer is requested.

## Steps

1. Push top-level items onto a stack in reverse order.
2. Before next/hasNext, peel list nodes until the top is an integer.
3. Pop and return integers; advance through nested children incrementally.
