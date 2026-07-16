# 2638. Count the Number of K-Free Subsets

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/count-the-number-of-k-free-subsets/](https://leetcode.com/problems/count-the-number-of-k-free-subsets/)
- **Premium:** Yes
- **Tags:** array, math, dynamic-programming, sorting, combinatorics

## Problem

You are given an integer array `nums`, which contains **distinct** elements and an integer `k`.

A subset is called a **k-Free** subset if it contains **no** two elements with an absolute difference equal to `k`. Notice that the empty set is a **k-Free** subset.

Return *the number of **k-Free** subsets of *`nums`.

A **subset** of an array is a selection of elements (possibly none) of the array.



**Example 1:**

**Input:** nums = [5,4,6], k = 1
**Output:** 5
**Explanation:** There are 5 valid subsets: {}, {5}, {4}, {6} and {4, 6}.

**Example 2:**

**Input:** nums = [2,3,5,8], k = 5
**Output:** 12
**Explanation:** There are 12 valid subsets: {}, {2}, {3}, {5}, {8}, {2, 3}, {2, 3, 5}, {2, 5}, {2, 5, 8}, {2, 8}, {3, 5} and {5, 8}.

**Example 3:**

**Input:** nums = [10,5,9,11], k = 20
**Output:** 16
**Explanation:** All subsets are valid. Since the total count of subsets is 2^{4 }= 16, so the answer is 16.



**Constraints:**

	- `1 <= nums.length <= 50`

	- `1 <= nums[i] <= 1000`

	- `1 <= k <= 1000`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Split all numbers into several groups, with each group being an arithmetic sequence with a common difference of k.
2. How many K-free subsets are there for each group? This can be solved by dp: dp[i] = dp[i-1] + dp[i-2], meaning if we choose ith element, we cannot choose (i-1)th; otherwise we can choose (i-1)th element.
3. After solving the problem for every group, the final result is just the product of the sub-problems.

## Approach

<!-- Describe your solution approach here -->
