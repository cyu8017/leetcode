# How We Solve Equal Tree Partition

Check whether any edge cut yields two components with equal sum.

## Steps

1. Compute every subtree sum via DFS.
2. Drop the full-tree sum; keep the rest.
3. Succeed if total is even and `total/2` appears as some proper subtree sum.
