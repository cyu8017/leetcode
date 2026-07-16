# 1655. Distribute Repeating Integers

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/distribute-repeating-integers/](https://leetcode.com/problems/distribute-repeating-integers/)
- **Tags:** array, hash-table, dynamic-programming, backtracking, bit-manipulation, counting, bitmask

## Problem

You are given an array of `n` integers, `nums`, where there are at most `50` unique values in the array. You are also given an array of `m` customer order quantities, `quantity`, where `quantity[i]` is the amount of integers the `i^{th}` customer ordered. Determine if it is possible to distribute `nums` such that:

- The `i^{th}` customer gets **exactly** `quantity[i]` integers,

	- The integers the `i^{th}` customer gets are **all equal**, and

	- Every customer is satisfied.

Return `true`* if it is possible to distribute *`nums`* according to the above conditions*.

**Example 1:**

```
**Input:** nums = [1,2,3,4], quantity = [2]
**Output:** false
**Explanation:** The 0^{th} customer cannot be given two different integers.
```

**Example 2:**

```
**Input:** nums = [1,2,3,3], quantity = [2]
**Output:** true
**Explanation:** The 0^{th} customer is given [3,3]. The integers [1,2] are not used.
```

**Example 3:**

```
**Input:** nums = [1,1,2,2], quantity = [2,2]
**Output:** true
**Explanation:** The 0^{th} customer is given [1,1], and the 1st customer is given [2,2].
```

**Constraints:**

- `n == nums.length`

	- `1 <= n <= 10^{5}`

	- `1 <= nums[i] <= 1000`

	- `m == quantity.length`

	- `1 <= m <= 10`

	- `1 <= quantity[i] <= 10^{5}`

	- There are at most `50` unique values in `nums`.

### Hints

1. Count the frequencies of each number. For example, if nums = [4,4,5,5,5], frequencies = [2,3].
2. Each customer wants all of their numbers to be the same. This means that each customer will be assigned to one number.
3. Use dynamic programming. Iterate through the numbers' frequencies, and choose some subset of customers to be assigned to this number.

## Approach

<!-- Describe your solution approach here -->
