# 1182. Shortest Distance to Target Color

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/shortest-distance-to-target-color/](https://leetcode.com/problems/shortest-distance-to-target-color/)
- **Premium:** Yes
- **Tags:** array, binary-search, dynamic-programming

## Problem

You are given an array `colors`, in which there are three colors: `1`, `2` and `3`.

You are also given some queries. Each query consists of two integers `i` and `c`, return the shortest distance between the given index `i` and the target color `c`. If there is no solution return `-1`.



**Example 1:**

**Input:** colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
**Output:** [3,0,3]
**Explanation: **
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).

**Example 2:**

**Input:** colors = [1,2], queries = [[0,3]]
**Output:** [-1]
**Explanation: **There is no 3 in the array.



**Constraints:**

	- `1 <= colors.length <= 5*10^4`

	- `1 <= colors[i] <= 3`

	- `1 <= queries.length <= 5*10^4`

	- `queries[i].length == 2`

	- `0 <= queries[i][0] < colors.length`

	- `1 <= queries[i][1] <= 3`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Greedy solution is too slow because of the limits.
2. Can you solve this problem offline by doing some pre-processing?
3. Calculate the answers for all indexes moving to their left and to their right.

## Approach

<!-- Describe your solution approach here -->
