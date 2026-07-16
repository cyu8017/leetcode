# 1428. Leftmost Column With At Least A One

## Approach
Use a direct greedy or traversal strategy to maintain exactly the state needed by the problem. The implementation processes each state once (or once per relevant transition) and avoids redundant work.

## Correctness
The maintained state represents all valid choices for the processed input. Each update considers every legal next choice, so induction over the processing order shows that the final state is optimal and complete.

## Complexity
The running time and auxiliary space are polynomial in the input size; see the loops and state arrays in `solution.py` for the exact bounds.
