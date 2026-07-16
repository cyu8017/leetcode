# 0573. Squirrel Simulation

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/squirrel-simulation/](https://leetcode.com/problems/squirrel-simulation/)
- **Premium:** Yes
- **Tags:** array, math

## Problem

You are given two integers `height` and `width` representing a garden of size `height x width`. You are also given:

	- an array `tree` where `tree = [tree_{r}, tree_{c}]` is the position of the tree in the garden,

	- an array `squirrel` where `squirrel = [squirrel_{r}, squirrel_{c}]` is the position of the squirrel in the garden,

	- and an array `nuts` where `nuts[i] = [nut_{ir}, nut_{ic}]` is the position of the `i^{th}` nut in the garden.

The squirrel can only take at most one nut at one time and can move in four directions: up, down, left, and right, to the adjacent cell.

Return *the **minimal distance** for the squirrel to collect all the nuts and put them under the tree one by one*.

The **distance** is the number of moves.



**Example 1:**

**Input:** height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0], [2,5]]
**Output:** 12
**Explanation:** The squirrel should go to the nut at [2, 5] first to achieve a minimal distance.

**Example 2:**

**Input:** height = 1, width = 3, tree = [0,1], squirrel = [0,0], nuts = [[0,2]]
**Output:** 3



**Constraints:**

	- `1 <= height, width <= 100`

	- `tree.length == 2`

	- `squirrel.length == 2`

	- `1 <= nuts.length <= 5000`

	- `nuts[i].length == 2`

	- `0 r} <= height`

	- `0 c} <= width`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Will Brute force solution works here? What will be its complexity?
2. Brute force definitely won't work here. Think of some simple solution. Take some example and make some observations.
3. Will order of nuts traversed by squirrel is important or only first nut traversed by squirrel is important?
4. Are there some paths which squirrel have to cover in any case? If yes, what are they?
5. Did you notice only first nut traversed by squirrel matters? Obviously squirrel will choose first nut which will result in minimum distance.

## Approach

<!-- Describe your solution approach here -->
