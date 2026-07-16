# 3018. Maximum Number of Removal Queries That Can Be Processed I

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/](https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/)
- **Premium:** Yes
- **Tags:** array, dynamic-programming

## Problem

You are given a **0-indexed** array `nums` and a **0-indexed** array `queries`.

You can do the following operation at the beginning **at most once**:

	- Replace `nums` with a subsequence of `nums`.

We start processing queries in the given order; for each query, we do the following:

	- If the first **and** the last element of `nums` is **less than** `queries[i]`, the processing of queries **ends**.

	- Otherwise, we choose either the first **or** the last element of `nums` if it is **greater than or equal to** `queries[i]`, and we **remove** the chosen element from `nums`.

Return *the **maximum** number of queries that can be processed by doing the operation optimally.*



**Example 1:**

**Input:** nums = [1,2,3,4,5], queries = [1,2,3,4,6]
**Output:** 4
**Explanation:** We don't do any operation and process the queries as follows:
1- We choose and remove nums[0] since 1

**Example 2:**

**Input:** nums = [2,3,2], queries = [2,2,3]
**Output:** 3
**Explanation:** We don't do any operation and process the queries as follows:
1- We choose and remove nums[0] since 2

**Example 3:**

**Input:** nums = [3,4,3], queries = [4,3,2]
**Output:** 2
**Explanation:** First we replace nums with the subsequence of nums [4,3].
Then we can process the queries as follows:
1- We choose and remove nums[0] since 4



**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= queries.length <= 1000`

	- `1 <= nums[i], queries[i] <= 10^{9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Think of dynamic programming.
2. The definition of `dp` is a little unusual. Try to think more.
3. Let `dp[l][r]` be the maximum number of queries we can process if we want `a[l], a[l + 1], ..., a[r - 1]` not to be removed after processing `dp[l][r]` queries.
4. So `dp[0][n] = 0` since we can not remove anything.
5. The answer would be `max(dp[i][i])`.

## Approach

<!-- Describe your solution approach here -->
