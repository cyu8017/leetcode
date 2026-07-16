# 2271. Maximum White Tiles Covered by a Carpet

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/](https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/)
- **Tags:** array, binary-search, greedy, sliding-window, sorting, prefix-sum

## Problem

You are given a 2D integer array `tiles` where `tiles[i] = [l_{i}, r_{i}]` represents that every tile `j` in the range `l_{i} <= j <= r_{i}` is colored white.

You are also given an integer `carpetLen`, the length of a single carpet that can be placed **anywhere**.

Return *the **maximum** number of white tiles that can be covered by the carpet*.

**Example 1:**

```
**Input:** tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
**Output:** 9
**Explanation:** Place the carpet starting on tile 10.
It covers 9 white tiles, so we return 9.
Note that there may be other places where the carpet covers 9 white tiles.
It can be shown that the carpet cannot cover more than 9 white tiles.
```

**Example 2:**

```
**Input:** tiles = [[10,11],[1,1]], carpetLen = 2
**Output:** 2
**Explanation:** Place the carpet starting on tile 10.
It covers 2 white tiles, so we return 2.
```

**Constraints:**

- `1 <= tiles.length <= 5 * 10^{4}`

	- `tiles[i].length == 2`

	- `1 <= l_{i} <= r_{i} <= 10^{9}`

	- `1 <= carpetLen <= 10^{9}`

	- The `tiles` are **non-overlapping**.

### Hints

1. Think about the potential placements of the carpet in an optimal solution.
2. Can we use Prefix Sum and Binary Search to determine how many tiles are covered for a given placement?

## Approach

<!-- Describe your solution approach here -->
