# How We Solve N-ary Tree Level Order Traversal

Standard BFS processes one level at a time by snapshotting the queue size before dequeuing.

## Steps

1. Start with the root in a queue.
2. For each level, dequeue exactly the current queue length.
3. Append each node's value and enqueue all of its children.
4. Push the collected level into the result and repeat until empty.
