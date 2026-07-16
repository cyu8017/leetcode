# How We Solve Serialize and Deserialize N-ary Tree

Breadth-first encoding stores each node value, its child count, then its child values in order.

## Steps

1. BFS over the tree, appending `value, childCount, childValues...` for each node.
2. Decode by reading the root record, enqueueing placeholder child nodes.
3. Fill each queued node by reading its own count and child values from the stream.
