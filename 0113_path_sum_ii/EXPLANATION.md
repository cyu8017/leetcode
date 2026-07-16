# How We Solve Path Sum II

Collect every root-to-leaf path that sums to the target.

## Steps

1. DFS with the remaining sum and the path so far.
2. Push the current node value onto the path.
3. At a leaf whose value matches the remaining sum, copy the path.
4. Otherwise recurse into both children with a reduced remaining sum.
5. Pop after exploring so sibling branches share the same buffer.
