# 2345. Finding the Number of Visible Mountains

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/finding-the-number-of-visible-mountains/](https://leetcode.com/problems/finding-the-number-of-visible-mountains/)
- **Premium:** Yes
- **Tags:** array, stack, sorting, monotonic-stack

## Problem

You are given a **0-indexed** 2D integer array `peaks` where `peaks[i] = [x_{i}, y_{i}]` states that mountain `i` has a peak at coordinates `(x_{i}, y_{i})`. A mountain can be described as a right-angled isosceles triangle, with its base along the `x`-axis and a right angle at its peak. More formally, the **gradients** of ascending and descending the mountain are `1` and `-1` respectively.

A mountain is considered **visible** if its peak does not lie within another mountain (including the border of other mountains).

Return *the number of visible mountains*.



**Example 1:**

**Input:** peaks = [[2,2],[6,3],[5,4]]
**Output:** 2
**Explanation:** The diagram above shows the mountains.
- Mountain 0 is visible since its peak does not lie within another mountain or its sides.
- Mountain 1 is not visible since its peak lies within the side of mountain 2.
- Mountain 2 is visible since its peak does not lie within another mountain or its sides.
There are 2 mountains that are visible.

**Example 2:**

**Input:** peaks = [[1,3],[1,3]]
**Output:** 0
**Explanation:** The diagram above shows the mountains (they completely overlap).
Both mountains are not visible since their peaks lie within each other.



**Constraints:**

	- `1 <= peaks.length <= 10^{5}`

	- `peaks[i].length == 2`

	- `1 <= x_{i}, y_{i} <= 10^{5}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. How can we efficiently find for each mountain the relevant mountains to compare itself against to check whether or not it would be visible?
2. Do you notice a pattern after sorting the peaks by their x-coordinates?
3. After sorting, process the peaks sequentially and use a monotonic stack to store currently visible mountains.

## Approach

<!-- Describe your solution approach here -->
