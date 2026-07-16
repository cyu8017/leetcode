# How We Solve Employee Importance

DFS (or BFS) from the target employee, summing importance down the subordinate tree.

## Steps

1. Index employees by id (supports list or `Employee` objects).
2. Recursively add each employee’s importance plus all subordinates.
3. Return the total for the given id.
