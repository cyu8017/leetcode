# How We Solve Add Two Numbers

Two numbers are stored as linked lists (digits from right to left, like beads).

## Steps

1. Start at the first bead of both lists.
2. Add the two digits plus any carry (like 7+8=15, carry the 1).
3. Make a new bead with the ones digit of the sum.
4. Move to the next beads and repeat.
5. Keep going until both lists are done and carry is zero.
6. Return the new list.
