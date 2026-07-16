# How We Solve Find Duplicate Subtrees

Serialize every subtree and count identical serializations.

## Steps

1. Postorder stringify each node as `val,left,right` (null as `#`).
2. Increment a count for each serialization.
3. When a serialization is seen the second time, record that node as a duplicate.
