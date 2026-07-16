# How We Solve Course Schedule

Kahn's algorithm detects whether the prerequisite graph is a DAG.

## Steps

1. Build an adjacency list and indegree array.
2. Queue every course with indegree 0.
3. Take courses one by one and reduce neighbors' indegrees.
4. Enqueue neighbors that reach indegree 0.
5. Succeed only if every course was taken.
