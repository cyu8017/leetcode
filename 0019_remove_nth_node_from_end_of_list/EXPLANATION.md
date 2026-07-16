# How We Solve Remove Nth Node From End of List

Remove the node n steps from the **end** of a linked list.

## Steps

1. Put a dummy head before the list (helps when removing the first node).
2. Move a fast finger n steps ahead.
3. Move fast and slow together until fast reaches the end.
4. Slow is now just before the node to remove.
5. Skip that node by linking around it.
6. Return the list after dummy.
