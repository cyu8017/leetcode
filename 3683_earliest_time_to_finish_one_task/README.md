# 3683. Earliest Time to Finish One Task

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/earliest-time-to-finish-one-task/](https://leetcode.com/problems/earliest-time-to-finish-one-task/)
- **Tags:** array

## Problem

You are given a 2D integer array `tasks` where `tasks[i] = [s_{i}, t_{i}]`.

Each `[s_{i}, t_{i}]` in `tasks` represents a task with start time `s_{i}` that takes `t_{i}` units of time to finish.

Return the earliest time at which at least one task is finished.

**Example 1:**

**Input:** tasks = [[1,6],[2,3]]

**Output:** 5

**Explanation:**

The first task starts at time `t = 1` and finishes at time `1 + 6 = 7`. The second task finishes at time `2 + 3 = 5`. You can finish one task at time 5.

**Example 2:**

**Input:** tasks = [[100,100],[100,100],[100,100]]

**Output:** 200

**Explanation:**

All three tasks finish at time `100 + 100 = 200`.

**Constraints:**

- `1 <= tasks.length <= 100`

	- `tasks[i] = [s_{i}, t_{i}]`

	- `1 <= s_{i}, t_{i} <= 100`

### Hints

1. Compute `finish[i] = s[i] + t[i]` for each task and take the minimum.

## Approach

<!-- Describe your solution approach here -->
