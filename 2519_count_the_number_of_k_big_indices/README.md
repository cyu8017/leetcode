# 2519. Count the Number of K-Big Indices

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/count-the-number-of-k-big-indices/](https://leetcode.com/problems/count-the-number-of-k-big-indices/)
- **Premium:** Yes
- **Tags:** array, binary-search, divide-and-conquer, binary-indexed-tree, segment-tree, merge-sort, ordered-set

## Problem

You are given a **0-indexed** integer array `nums` and a positive integer `k`.

We call an index `i` **k-big** if the following conditions are satisfied:

	- There exist at least `k` different indices `idx1` such that `idx1 < i` and `nums[idx1] < nums[i]`.

	- There exist at least `k` different indices `idx2` such that `idx2 > i` and `nums[idx2] < nums[i]`.

Return *the number of k-big indices*.



**Example 1:**

**Input:** nums = [2,3,6,5,2,3], k = 2
**Output:** 2
**Explanation:** There are only two 2-big indices in nums:
- i = 2 --> There are two valid idx1: 0 and 1. There are three valid idx2: 2, 3, and 4.
- i = 3 --> There are two valid idx1: 0 and 1. There are two valid idx2: 3 and 4.

**Example 2:**

**Input:** nums = [1,1,1], k = 3
**Output:** 0
**Explanation:** There are no 3-big indices in nums.



**Constraints:**

	- `1 <= nums.length <= 10^{5}`

	- `1 <= nums[i], k <= nums.length`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. The intended solution uses Fenwick Tree.
2. Let’s describe the solution for counting the number of elements smaller than nums[i] in the range [0, i - 1], and counting in the range [i + 1, nums.length - 1] can be done similarly by simply reversing the array.
3. Iterate from left to right and maintain the Fenwick Tree. Save the value of the query(nums[i]) and update nums[i] + 1 by 1.

## Approach

<!-- Describe your solution approach here -->
