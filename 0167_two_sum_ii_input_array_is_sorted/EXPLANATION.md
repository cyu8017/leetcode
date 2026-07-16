# How We Solve Two Sum II

Two pointers on the sorted array find the unique pair.

## Steps

1. Start left at the beginning and right at the end.
2. Compare their sum with the target.
3. Move left up when the sum is too small.
4. Move right down when the sum is too large.
5. Return the 1-indexed positions when they match.
