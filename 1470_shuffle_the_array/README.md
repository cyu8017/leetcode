# 1470. Shuffle the Array

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/shuffle-the-array/](https://leetcode.com/problems/shuffle-the-array/)
- **Tags:** array

## Problem

Given the array `nums` consisting of `2n` elements in the form `[x_{1},x_{2},...,x_{n},y_{1},y_{2},...,y_{n}]`.

*Return the array in the form* `[x_{1},y_{1},x_{2},y_{2},...,x_{n},y_{n}]`.

**Example 1:**

```
**Input:** nums = [2,5,1,3,4,7], n = 3
**Output:** [2,3,5,4,1,7]
**Explanation:** Since x_{1}=2, x_{2}=5, x_{3}=1, y_{1}=3, y_{2}=4, y_{3}=7 then the answer is [2,3,5,4,1,7].
```

**Example 2:**

```
**Input:** nums = [1,2,3,4,4,3,2,1], n = 4
**Output:** [1,4,2,3,3,2,4,1]
```

**Example 3:**

```
**Input:** nums = [1,1,2,2], n = 2
**Output:** [1,2,1,2]
```

**Constraints:**

- `1 <= n <= 500`

	- `nums.length == 2n`

	- `1 <= nums[i] <= 10^3`

### Hints

1. Use two pointers to create the new array of 2n elements. The first starting at the beginning and the other starting at (n+1)th position. Alternate between them and create the new array.

## Approach

<!-- Describe your solution approach here -->
