# How We Solve Palindrome Linked List

Find the middle, reverse the second half, then compare both halves.

## Steps

1. Use slow and fast pointers to reach the middle.
2. Reverse the second half of the list.
3. Walk the first half and reversed second half together.
4. Compare values at each step.
5. Return false on the first mismatch, otherwise true.
