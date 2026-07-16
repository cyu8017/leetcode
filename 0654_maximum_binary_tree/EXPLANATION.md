# How We Solve Maximum Binary Tree

Recursively build: root is the maximum in the subarray; left/right recurse on partitions.

## Steps

1. Find the max index in `[left, right]`.
2. Root = that value; left subtree from left of max; right from right of max.
3. Empty range yields null.
