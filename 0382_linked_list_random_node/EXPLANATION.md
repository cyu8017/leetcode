# How We Solve Linked List Random Node

Reservoir sampling picks each node with equal probability in one pass.

## Steps

1. Walk the list once, collecting node values.
2. On each getRandom call, choose uniformly from the collected nodes.
3. Constructor stores the list head for repeated sampling.
