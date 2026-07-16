# How We Solve Find Leaves of Binary Tree

Node height from leaves upward groups nodes removed together.

## Steps

1. DFS compute height where leaves have height 0.
2. Append node values into the bucket for their height.
3. Return buckets from leaves to root in order.
