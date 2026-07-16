# 1229. Meeting Scheduler

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/meeting-scheduler/](https://leetcode.com/problems/meeting-scheduler/)
- **Premium:** Yes
- **Tags:** array, two-pointers, sorting

## Problem

Given the availability time slots arrays `slots1` and `slots2` of two people and a meeting duration `duration`, return the **earliest time slot** that works for both of them and is of duration `duration`.

If there is no common time slot that satisfies the requirements, return an **empty array**.

The format of a time slot is an array of two elements `[start, end]` representing an inclusive time range from `start` to `end`.

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots `[start1, end1]` and `[start2, end2]` of the same person, either `start1 > end2` or `start2 > end1`.



**Example 1:**

**Input:** slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
**Output:** [60,68]

**Example 2:**

**Input:** slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
**Output:** []



**Constraints:**

	- `1 <= slots1.length, slots2.length <= 10^{4}`

	- `slots1[i].length, slots2[i].length == 2`

	- `slots1[i][0] < slots1[i][1]`

	- `slots2[i][0] < slots2[i][1]`

	- `0 <= slots1[i][j], slots2[i][j] <= 10^{9}`

	- `1 <= duration <= 10^{6}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Assume that in the solution, the selected slot from slotsA is bigger than the respectively selected slot from slotsB.
2. Use two pointers in order to try all the possible intersections, and check the length.
3. Do the same in step N° 1 but now assume that the selected slot from slotsB is bigger, return the minimum of the two options.

## Approach

<!-- Describe your solution approach here -->
