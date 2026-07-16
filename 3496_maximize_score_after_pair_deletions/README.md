# 3496. Maximize Score After Pair Deletions

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/maximize-score-after-pair-deletions/](https://leetcode.com/problems/maximize-score-after-pair-deletions/)
- **Premium:** Yes
- **Tags:** array, greedy

## Problem

You are given an array of integers `nums`. You **must** repeatedly perform one of the following operations while the array has more than two elements:

	- Remove the first two elements.

	- Remove the last two elements.

	- Remove the first and last element.

For each operation, add the sum of the removed elements to your total score.

Return the **maximum** possible score you can achieve.



**Example 1:**

**Input:** nums = [2,4,1]

**Output:** 6

**Explanation:**

The possible operations are:

	- Remove the first two elements `(2 + 4) = 6`. The remaining array is `[1]`.

	- Remove the last two elements `(4 + 1) = 5`. The remaining array is `[2]`.

	- Remove the first and last elements `(2 + 1) = 3`. The remaining array is `[4]`.

The maximum score is obtained by removing the first two elements, resulting in a final score of 6.

**Example 2:**

**Input:** nums = [5,-1,4,2]

**Output:** 7

**Explanation:**

The possible operations are:

	- Remove the first and last elements `(5 + 2) = 7`. The remaining array is `[-1, 4]`.

	- Remove the first two elements `(5 + -1) = 4`. The remaining array is `[4, 2]`.

	- Remove the last two elements `(4 + 2) = 6`. The remaining array is `[5, -1]`.

The maximum score is obtained by removing the first and last elements, resulting in a total score of 7.



**Constraints:**

	- `1 <= nums.length <= 10^{5}`

	- `-10^{4} <= nums[i] <= 10^{4}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. The number of operations is `floor((n - 1) / 2)`, so the number of remaining elements is `n - 2 * floor((n - 1) / 2)`.
2. There will be either 1 or 2 elements remaining.
3. If there is 1 element remaining, let it be the minimum element.
4. If there are 2 elements remaining, let them be the adjacent elements with the minimum sum.

## Approach

<!-- Describe your solution approach here -->
