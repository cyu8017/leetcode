# 3632. Subarrays with XOR at Least K

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/subarrays-with-xor-at-least-k/](https://leetcode.com/problems/subarrays-with-xor-at-least-k/)
- **Premium:** Yes
- **Tags:** array, bit-manipulation, trie, prefix-sum

## Problem

Given an array of positive integers nums of length n and a non‑negative integer k.

Return the number of **contiguous subarrays** whose bitwise XOR of all elements is **greater** than or **equal** to k.



**Example 1:**

**Input:** nums = [3,1,2,3], k = 2

**Output:** 6

**Explanation:**

The valid subarrays with `XOR >= 2` are `[3]` at index 0, `[3, 1]` at indices 0 - 1, `[3, 1, 2, 3]` at indices 0 - 3, `[1, 2]` at indices 1 - 2, `[2]` at index 2, and `[3]` at index 3; there are 6 in total.

**Example 2:**

**Input:** nums = [0,0,0], k = 0

**Output:** 6

**Explanation:**

Every contiguous subarray yields `XOR = 0`, which meets `k = 0`. There are 6 such subarrays in total.



**Constraints:**

	1

	0

	0

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use a prefix XOR array
2. For each ending index, count how many subarrays have `XOR >= k`
3. Use a Trie to query those counts efficiently

## Approach

<!-- Describe your solution approach here -->
