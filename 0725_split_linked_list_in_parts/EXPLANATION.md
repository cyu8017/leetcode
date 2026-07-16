# How We Solve Split Linked List in Parts

Divide `n` nodes into `k` parts of size `n//k` or `n//k+1`.

## Steps

1. Count the list length.
2. The first `n % k` parts get one extra node.
3. Cut the list into those lengths, padding with `null` if needed.
