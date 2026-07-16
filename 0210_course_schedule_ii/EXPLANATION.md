# How We Solve Course Schedule II

Kahn's BFS produces a valid topological order of courses.

## Steps

1. Build the graph and indegree counts from prerequisites.
2. Queue all courses with indegree 0.
3. Append each dequeued course to the order.
4. Reduce indegrees of dependents and enqueue newly ready courses.
5. Return the order if it contains every course, otherwise an empty list.
