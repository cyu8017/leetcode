# How We Solve Implement Queue using Stacks

Use an input stack and an output stack to reverse order on demand.

## Steps

1. Push new items onto the input stack.
2. When popping or peeking, move items to the output stack if it is empty.
3. Each move reverses order once, giving FIFO behavior.
4. Pop and peek from the output stack top.
5. Empty means both stacks are empty.
