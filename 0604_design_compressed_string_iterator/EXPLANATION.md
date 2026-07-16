# How We Solve Design Compressed String Iterator

Parse letter/count pairs up front and walk them as an iterator.

## Steps

1. Split the compressed string into characters and repetition counts.
2. `next` emits the current character and decrements its remaining count.
3. `hasNext` reports whether any characters remain.
