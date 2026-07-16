# 0360. Sort Transformed Array

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/sort-transformed-array/](https://leetcode.com/problems/sort-transformed-array/)
- **Premium:** Yes
- **Tags:** array, math, two-pointers, sorting

## Problem

Given a **sorted** integer array `nums` and three integers `a`, `b` and `c`, apply a quadratic function of the form `f(x) = ax^{2} + bx + c` to each element `nums[i]` in the array, and return *the array in a sorted order*.



**Example 1:**

**Input:** nums = [-4,-2,2,4], a = 1, b = 3, c = 5
**Output:** [3,9,15,33]

**Example 2:**

**Input:** nums = [-4,-2,2,4], a = -1, b = 3, c = 5
**Output:** [-23,-5,1,7]



**Constraints:**

	- `1 <= nums.length <= 200`

	- `-100 <= nums[i], a, b, c <= 100`

	- `nums` is sorted in **ascending** order.



**Follow up:** Could you solve it in `O(n)` time?

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. x^2 + x  will form a parabola.
2. Parameter A in:  A * x^2 + B * x + C dictates the shape of the parabola.
Positive A means the parabola remains concave (high-low-high), but negative A inverts the parabola to be convex (low-high-low).

## Approach

<!-- Describe your solution approach here -->
