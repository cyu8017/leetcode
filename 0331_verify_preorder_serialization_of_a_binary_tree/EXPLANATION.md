# How We Solve Verify Preorder Serialization of a Binary Tree

Slot counting tracks whether the preorder stream can close a valid tree.

## Steps

1. Start with one open slot for the root.
2. Each node consumes one slot; internal nodes add two child slots.
3. Null markers only consume slots. Valid iff slots reach zero at the end.
