# How We Solve Maximum XOR of Two Numbers in an Array

Build a binary trie of all numbers, then for each value walk the trie preferring the opposite bit at every level.

## Steps

1. Insert every number into a bit trie from the highest set bit down.
2. For each number, greedily choose the complementary bit when a branch exists.
3. Track the maximum XOR value found across all pairs.
