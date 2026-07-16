# 1499. Max Value of Equation

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/max-value-of-equation/](https://leetcode.com/problems/max-value-of-equation/)
- **Tags:** array, queue, sliding-window, heap-(priority-queue), monotonic-queue

## Problem

You are given an array `points` containing the coordinates of points on a 2D plane, sorted by the x-values, where `points[i] = [x_{i}, y_{i}]` such that `x_{i} < x_{j}` for all `1 <= i < j <= points.length`. You are also given an integer `k`.

Return *the maximum value of the equation *`y_{i} + y_{j} + |x_{i} - x_{j}|` where `|x_{i} - x_{j}| <= k` and `1 <= i < j <= points.length`.

It is guaranteed that there exists at least one pair of points that satisfy the constraint `|x_{i} - x_{j}| <= k`.

**Example 1:**

```
**Input:** points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
**Output:** 4
**Explanation:** The first two points satisfy the condition |x_{i} - x_{j}| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
```

**Example 2:**

```
**Input:** points = [[0,0],[3,0],[9,2]], k = 3
**Output:** 3
**Explanation: **Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
```

**Constraints:**

- `2 <= points.length <= 10^{5}`

	- `points[i].length == 2`

	- `-10^{8} <= x_{i}, y_{i} <= 10^{8}`

	- `0 <= k <= 2 * 10^{8}`

	- `x_{i} < x_{j}` for all `1 <= i < j <= points.length`

	- `x_{i}` form a strictly increasing sequence.

### Hints

1. Use a priority queue to store for each point i, the tuple [yi-xi, xi]
2. Loop through the array and pop elements from the heap if the condition xj - xi > k, where j is the current index and i is the point on top the queue.
3. After popping elements from the queue. If the queue is not empty, calculate the equation with the current point and the point on top of the queue and maximize the answer.

## Approach

<!-- Describe your solution approach here -->
