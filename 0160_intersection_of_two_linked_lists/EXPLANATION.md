# How We Solve Intersection of Two Linked Lists

Two pointers switch heads so both travel the same total distance.

## Steps

1. Start one pointer on each list.
2. Advance both one step at a time.
3. When a pointer reaches the end, redirect it to the other list's head.
4. They meet at the intersection, or both become null.
5. Return that meeting node.
