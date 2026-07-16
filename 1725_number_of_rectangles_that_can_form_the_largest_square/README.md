# 1725. Number Of Rectangles That Can Form The Largest Square

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/](https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/)
- **Tags:** array

## Problem

You are given an array `rectangles` where `rectangles[i] = [l_{i}, w_{i}]` represents the `i^{th}` rectangle of length `l_{i}` and width `w_{i}`.

You can cut the `i^{th}` rectangle to form a square with a side length of `k` if both `k <= l_{i}` and `k <= w_{i}`. For example, if you have a rectangle `[4,6]`, you can cut it to get a square with a side length of at most `4`.

Let `maxLen` be the side length of the **largest** square you can obtain from any of the given rectangles.

Return *the **number** of rectangles that can make a square with a side length of *`maxLen`.

**Example 1:**

```
**Input:** rectangles = [[5,8],[3,9],[5,12],[16,5]]
**Output:** 3
**Explanation:** The largest squares you can get from each rectangle are of lengths [5,3,5,5].
The largest possible square is of length 5, and you can get it out of 3 rectangles.
```

**Example 2:**

```
**Input:** rectangles = [[2,3],[3,7],[4,3],[3,7]]
**Output:** 3
```

**Constraints:**

- `1 <= rectangles.length <= 1000`

	- `rectangles[i].length == 2`

	- `1 <= l_{i}, w_{i} <= 10^{9}`

	- `l_{i} != w_{i}`

### Hints

1. What is the length of the largest square the can be cut out of some rectangle? It'll be equal to min(rectangle.length, rectangle.width). Replace each rectangle with this value.
2. Calculate maxSize by iterating over the given rectangles and maximizing the answer with their values denoted in the first hint.
3. Then iterate again on the rectangles and calculate the number whose values = maxSize.

## Approach

<!-- Describe your solution approach here -->
