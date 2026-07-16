# How We Solve Walls and Gates

Multi-source BFS from every gate fills empty rooms with distance.

## Steps

1. Enqueue all cells with distance zero (gates).
2. BFS to neighbors that are still empty (INF).
3. Set each reached room to parent distance plus one.
4. Stop when the queue is empty.
