# How We Solve Exclusive Time of Functions

Simulate the call stack, attributing time gaps to the currently running function.

## Steps

1. On `start`, credit the previous top of stack up to the new timestamp.
2. On `end`, credit the finishing function through the end timestamp inclusive.
3. Resume the next stack frame at `time + 1`.
