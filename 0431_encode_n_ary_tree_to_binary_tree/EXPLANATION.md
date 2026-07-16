# How We Solve Encode N-ary Tree to Binary Tree

Map the first N-ary child to the binary `left` pointer and link remaining siblings with `right`.

## Steps

1. Encode: binary left = first child, chain siblings via binary right pointers.
2. Decode: walk the left child and collect every node reached via right links as N-ary children.
3. Round-trip preserves the original tree structure.
