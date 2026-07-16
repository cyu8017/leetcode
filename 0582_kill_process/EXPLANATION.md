# How We Solve Kill Process

Build a parent-to-children map, then BFS from the kill target.

## Steps

1. Index every process under its parent id.
2. Start a queue at `kill`.
3. Collect each dequeued process and enqueue all of its children.
