# 1310. XOR Queries of a Subarray

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/xor-queries-of-a-subarray/](https://leetcode.com/problems/xor-queries-of-a-subarray/)
- **Tags:** array, bit-manipulation, prefix-sum

## Problem

You are given an array `arr` of positive integers. You are also given the array `queries` where `queries[i] = [left_{i, }right_{i}]`.

For each query `i` compute the **XOR** of elements from `left_{i}` to `right_{i}` (that is, `arr[left_{i}] XOR arr[left_{i} + 1] XOR ... XOR arr[right_{i}]` ).

Return an array `answer` where `answer[i]` is the answer to the `i^{th}` query.

**Example 1:**

```
**Input:** arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
**Output:** [2,7,14,8]
**Explanation:**
The binary representation of the elements in the array are:
1 = 0001
3 = 0011
4 = 0100
8 = 1000
The XOR values for queries are:
[0,1] = 1 xor 3 = 2
[1,2] = 3 xor 4 = 7
[0,3] = 1 xor 3 xor 4 xor 8 = 14
[3,3] = 8
```

**Example 2:**

```
**Input:** arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
**Output:** [8,0,4,4]
```

**Constraints:**

- `1 <= arr.length, queries.length <= 3 * 10^{4}`

	- `1 <= arr[i] <= 10^{9}`

	- `queries[i].length == 2`

	- `0 <= left_{i} <= right_{i} < arr.length`

### Hints

1. What is the result of x ^ y ^ x ?
2. Compute the prefix sum for XOR.
3. Process the queries with the prefix sum values.

## Approach

<!-- Describe your solution approach here -->
