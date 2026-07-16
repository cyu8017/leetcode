# How We Solve Delete Node in a Linked List

Copy the next node's value into the current node, then skip the next node.

## Steps

1. Read the value from the node after the target.
2. Copy that value into the target node.
3. Point the target node to the node after next.
4. This removes the next node instead of the target reference.
5. The list reflects the deletion without needing the head.
