# How We Solve Linked List Components

Count maximal contiguous runs of nodes whose values lie in `nums`.

## Steps

1. Put `nums` in a set.
2. Walk the list; start a component when entering a present value.
3. Increment once per contiguous run.
