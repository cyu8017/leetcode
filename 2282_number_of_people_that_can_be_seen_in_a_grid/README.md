# 2282. Number of People That Can Be Seen in a Grid

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/](https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/)
- **Premium:** Yes
- **Tags:** array, stack, matrix, monotonic-stack

## Problem

You are given an `m x n` **0-indexed** 2D array of positive integers `heights` where `heights[i][j]` is the height of the person standing at position `(i, j)`.

A person standing at position `(row_{1}, col_{1})` can see a person standing at position `(row_{2}, col_{2})` if:

	- The person at `(row_{2}, col_{2})` is to the right **or** below the person at `(row_{1}, col_{1})`. More formally, this means that either `row_{1} == row_{2}` and `col_{1} < col_{2}` **or** `row_{1} < row_{2}` and `col_{1} == col_{2}`.

	- Everyone in between them is shorter than **both** of them.

Return* an *`m x n`* 2D array of integers *`answer`* where *`answer[i][j]`* is the number of people that the person at position *`(i, j)`* can see.*



**Example 1:**

**Input:** heights = [[3,1,4,2,5]]
**Output:** [[2,1,2,1,0]]
**Explanation:**
- The person at (0, 0) can see the people at (0, 1) and (0, 2).
  Note that he cannot see the person at (0, 4) because the person at (0, 2) is taller than him.
- The person at (0, 1) can see the person at (0, 2).
- The person at (0, 2) can see the people at (0, 3) and (0, 4).
- The person at (0, 3) can see the person at (0, 4).
- The person at (0, 4) cannot see anybody.

**Example 2:**

**Input:** heights = [[5,1],[3,1],[4,1]]
**Output:** [[3,1],[2,1],[1,0]]
**Explanation:**
- The person at (0, 0) can see the people at (0, 1), (1, 0) and (2, 0).
- The person at (0, 1) can see the person at (1, 1).
- The person at (1, 0) can see the people at (1, 1) and (2, 0).
- The person at (1, 1) can see the person at (2, 1).
- The person at (2, 0) can see the person at (2, 1).
- The person at (2, 1) cannot see anybody.



**Constraints:**

	- `1 <= heights.length <= 400`

	- `1 <= heights[i].length <= 400`

	- `1 <= heights[i][j] <= 10^{5}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Imagine you are looking to the right. The heights of the people you see form an ascending sequence.
2. Iterate through the row from right to left. Use a decreasing monotonic stack to keep track of the people that you can see.
3. Use binary search to find the number of people in the stack that are shorter than the current person.
4. Repeat this process for each column.

## Approach

<!-- Describe your solution approach here -->
