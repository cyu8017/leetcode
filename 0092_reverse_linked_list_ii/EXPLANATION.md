# How We Solve Reverse Linked List II

Reverse only the part of a list between two positions.

## Steps

1. Put a dummy node before the head.
2. Walk to the node just before the left position.
3. Reverse the next (right − left) links by inserting at the front of that section.
4. Leave the rest of the list alone.
5. Return the list after the dummy.
