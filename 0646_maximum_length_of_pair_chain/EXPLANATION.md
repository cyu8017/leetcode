# How We Solve Maximum Length of Pair Chain

Greedily take pairs by earliest ending time, like interval scheduling.

## Steps

1. Sort pairs by right endpoint.
2. Append a pair when its left is strictly greater than the current chain end.
3. Return the number of pairs taken.
