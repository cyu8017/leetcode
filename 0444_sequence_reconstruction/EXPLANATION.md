# How We Solve Sequence Reconstruction

Build precedence edges from consecutive pairs in every subsequence, then check for a unique topological order.

## Steps

1. Add directed edges for each adjacent pair (deduplicated).
2. Run Kahn topological sort; fail if the queue ever has more than one choice.
3. Compare the resulting order with `org`.
