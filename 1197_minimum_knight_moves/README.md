# 1197. Minimum Knight Moves

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/minimum-knight-moves/](https://leetcode.com/problems/minimum-knight-moves/)
- **Premium:** Yes
- **Tags:** breadth-first-search

## Problem

In an **infinite** chess board with coordinates from `-infinity` to `+infinity`, you have a **knight** at square `[0, 0]`.

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return *the minimum number of steps needed to move the knight to the square* `[x, y]`. It is guaranteed the answer exists.



**Example 1:**

**Input:** x = 2, y = 1
**Output:** 1
**Explanation: **[0, 0] → [2, 1]

**Example 2:**

**Input:** x = 5, y = 5
**Output:** 4
**Explanation: **[0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]



**Constraints:**

	- `-300 <= x, y <= 300`

	- `0 <= |x| + |y| <= 300`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. You can simulate the movements since the limits are low.
2. Is there a search algorithm applicable to this problem?
3. Since we want the minimum number of moves, we can use Breadth First Search.

## Approach

<!-- Describe your solution approach here -->
