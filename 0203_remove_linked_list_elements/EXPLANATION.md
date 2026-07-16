# How We Solve Remove Linked List Elements

Walk a dummy-headed list and skip every node whose value matches the target.

## Steps

1. Attach a dummy node before the head.
2. Advance while looking at the next node.
3. If the next value equals the target, bypass that node.
4. Otherwise move forward one step.
5. Return dummy.next as the cleaned list.
