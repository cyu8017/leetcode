# How We Solve Binary Tree Maximum Path Sum

Any node-to-node path can bend at a root; DFS returns one-sided gain.

## Steps

1. Recurse into left and right, clamping negative gains to 0.
2. Candidate path through the node is value plus both gains.
3. Update a global best with that candidate.
4. Return value plus the better single child gain to the parent.
5. Answer is the global best after the DFS.
