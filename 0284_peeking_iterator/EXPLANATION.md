# How We Solve Peeking Iterator

Cache one lookahead value so peek does not consume the stream.

## Steps

1. On first peek, read from the underlying iterator into a buffer.
2. Return the buffer on subsequent peeks.
3. On next, return the buffer if present; otherwise read from the iterator.
4. hasNext is true if buffered or the underlying iterator has more.
