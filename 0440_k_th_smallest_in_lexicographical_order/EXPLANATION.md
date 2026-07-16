# How We Solve K-th Smallest in Lexicographical Order

Numbers form a 10-ary trie; count how many numbers live under each prefix.

## Steps

1. Start at prefix `1` and treat `k` as steps remaining (0-indexed).
2. Count numbers in the current prefix subtree versus the next sibling prefix.
3. Go deeper (×10) or move to the next sibling (+1) until `k` reaches zero.
