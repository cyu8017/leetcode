# How We Solve Path Sum

Ask whether any root-to-leaf path sums to the target.

## Steps

1. Empty tree has no path.
2. At a leaf, check whether the remaining sum equals the leaf value.
3. Otherwise subtract the current value and try left and right.
4. Succeed if either subtree finds a path.
5. Return that boolean answer.
