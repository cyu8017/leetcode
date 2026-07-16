# 2001. Number of Pairs of Interchangeable Rectangles

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/](https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/)
- **Tags:** array, hash-table, math, counting, number-theory

## Problem

You are given `n` rectangles represented by a **0-indexed** 2D integer array `rectangles`, where `rectangles[i] = [width_{i}, height_{i}]` denotes the width and height of the `i^{th}` rectangle.

Two rectangles `i` and `j` (`i < j`) are considered **interchangeable** if they have the **same** width-to-height ratio. More formally, two rectangles are **interchangeable** if `width_{i}/height_{i} == width_{j}/height_{j}` (using decimal division, not integer division).

Return *the **number** of pairs of **interchangeable** rectangles in *`rectangles`.

**Example 1:**

```
**Input:** rectangles = [[4,8],[3,6],[10,20],[15,30]]
**Output:** 6
**Explanation:** The following are the interchangeable pairs of rectangles by index (0-indexed):
- Rectangle 0 with rectangle 1: 4/8 == 3/6.
- Rectangle 0 with rectangle 2: 4/8 == 10/20.
- Rectangle 0 with rectangle 3: 4/8 == 15/30.
- Rectangle 1 with rectangle 2: 3/6 == 10/20.
- Rectangle 1 with rectangle 3: 3/6 == 15/30.
- Rectangle 2 with rectangle 3: 10/20 == 15/30.
```

**Example 2:**

```
**Input:** rectangles = [[4,5],[7,8]]
**Output:** 0
**Explanation:** There are no interchangeable pairs of rectangles.
```

**Constraints:**

- `n == rectangles.length`

	- `1 <= n <= 10^{5}`

	- `rectangles[i].length == 2`

	- `1 <= width_{i}, height_{i} <= 10^{5}`

### Hints

1. Store the rectangle height and width ratio in a hashmap.
2. Traverse the ratios, and for each ratio, use the frequency of the ratio to add to the total pair count.

## Approach

<!-- Describe your solution approach here -->
