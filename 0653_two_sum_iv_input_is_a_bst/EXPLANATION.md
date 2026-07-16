# How We Solve Two Sum IV - Input is a BST

DFS with a set of seen values; look for complement `k - node.val`.

## Steps

1. Walk the tree in any order.
2. If `k - node.val` was already seen, return true.
3. Otherwise add `node.val` and continue.
