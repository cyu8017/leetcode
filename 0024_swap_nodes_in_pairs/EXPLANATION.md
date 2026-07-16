# How We Solve Swap Nodes in Pairs

Swap every two nodes: 1->2->3->4 becomes 2->1->4->3.

## Steps

1. Use a dummy node before the head.
2. If two nodes exist, swap their links.
3. Move to the next unswapped pair.
4. Repeat until fewer than two nodes remain.
5. Return the list after dummy.
