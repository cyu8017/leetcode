# 2077. Paths in Maze That Lead to Same Room

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/](https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/)
- **Premium:** Yes
- **Tags:** graph-theory

## Problem

A maze consists of `n` rooms numbered from `1` to `n`, and some rooms are connected by corridors. You are given a 2D integer array `corridors` where `corridors[i] = [room1_{i}, room2_{i}]` indicates that there is a corridor connecting `room1_{i}` and `room2_{i}`, allowing a person in the maze to go from `room1_{i}` to `room2_{i}` **and vice versa**.

The designer of the maze wants to know how confusing the maze is. The **confusion** **score** of the maze is the number of different cycles of **length 3**.

	- For example, `1 → 2 → 3 → 1` is a cycle of length 3, but `1 → 2 → 3 → 4` and `1 → 2 → 3 → 2 → 1` are not.

Two cycles are considered to be **different** if one or more of the rooms visited in the first cycle is **not** in the second cycle.

Return *the* ***confusion**** score** of the maze.*



**Example 1:**

**Input:** n = 5, corridors = [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]]
**Output:** 2
**Explanation:**
One cycle of length 3 is 4 → 1 → 3 → 4, denoted in red.
Note that this is the same cycle as 3 → 4 → 1 → 3 or 1 → 3 → 4 → 1 because the rooms are the same.
Another cycle of length 3 is 1 → 2 → 4 → 1, denoted in blue.
Thus, there are two different cycles of length 3.

**Example 2:**

**Input:** n = 4, corridors = [[1,2],[3,4]]
**Output:** 0
**Explanation:**
There are no cycles of length 3.



**Constraints:**

	- `2 <= n <= 1000`

	- `1 <= corridors.length <= 5 * 10^{4}`

	- `corridors[i].length == 2`

	- `1 <= room1_{i}, room2_{i} <= n`

	- `room1_{i} != room2_{i}`

	- There are no duplicate corridors.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. If the path starts at room i, what properties must the other two rooms in the cycle have?
2. The other two rooms must be connected to room i, and must be connected to each other.

## Approach

<!-- Describe your solution approach here -->
