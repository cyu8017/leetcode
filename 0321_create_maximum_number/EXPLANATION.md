# How We Solve Create Maximum Number

Pick the best subsequence from each array, then merge lexicographically.

## Steps

1. Try every split of k digits between the two arrays.
2. Use a monotone stack to pick the largest subsequence of each length.
3. Merge pairs with suffix-aware comparison and keep the maximum.
