# How We Solve Min Stack

Keep a parallel mins stack so getMin stays O(1).

## Steps

1. On push, append the value and the new running minimum.
2. On pop, remove from both stacks together.
3. Top returns the last value on the main stack.
4. getMin returns the last value on the mins stack.
5. Every operation stays amortized constant time.
