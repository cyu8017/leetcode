# How We Solve Reverse Nodes in k-Group

Reverse every group of k nodes; leave a short tail unchanged.

## Steps

1. Walk k steps to find the end of the current group.
2. If fewer than k nodes remain, stop.
3. Reverse the k nodes inside the group.
4. Hook the reversed block back into the list.
5. Move to the next group and repeat.
6. Return the new head.
