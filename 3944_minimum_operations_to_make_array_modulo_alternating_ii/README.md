# 3944. Minimum Operations to Make Array Modulo Alternating II

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/](https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/)
- **Premium:** Yes
- **Tags:** array, enumeration

## Problem

You are given an integer array `nums` and an integer `k`.

In one operation, you can **increase** or **decrease** any element of `nums` by 1.

An array is called **modulo alternating** if there exist two **distinct** integers `x` and `y` (`0 <= x, y < k`) such that:

	- For every **even** index `i`, `nums[i] % k == x`

	- For every **odd** index `i`, `nums[i] % k == y`

Return the **minimum** number of operations required to make `nums` **modulo alternating**.



**Example 1:**

**Input:** nums = [1,4,2,8], k = 3

**Output:** 2

**Explanation:**

	- Let's choose `x = 1` for even indices and `y = 2` for odd indices.

	- Perform the following operations:


		- Increment `nums[1] = 4` by 1, giving `nums = [1, 5, 2, 8]`.

		- Decrement `nums[2] = 2` by 1, giving `nums = [1, 5, 1, 8]`.





	- Now, for even indices, `nums[i] % k = 1`, and for odd indices, `nums[i] % k = 2`.

	- Thus, the total number of operations required is 2.

**Example 2:**

**Input:** nums = [1,1,1], k = 3

**Output:** 1

**Explanation:**

	- Incrementing `nums[1]` by 1 gives `nums = [1, 2, 1]`, which satisfies the condition with `x = 1` and `y = 2`.

	- Thus, the total number of operations required is 1.

**Example 3:**

**Input:** nums = [6,7,8], k = 2

**Output:** 0

**Explanation:**

The array already satisfies the condition with `x = 0` and `y = 1`. Thus, no operations are required.



**Constraints:**

	- `1 <= nums.length <= 10^{5}`

	- `1 <= nums[i] <= 10^{9}`

	- `2 <= k <= 10^{5}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. For a number with remainder `r = nums[i] % k`, the minimum cost to change it to remainder `t` is:

`min(abs(r - t), k - abs(r - t))`
2. Separate the indices by parity. Compute

`evenCost[x]` = total cost to make all even indices have remainder `x`,
`oddCost[y]` = total cost to make all odd indices have remainder `y`
3. Then the answer is:

`min(evenCost[x] + oddCost[y])` over all `x != y`.
4. To avoid `O(k^{2})`, keep the smallest and second smallest values in `oddCost`. For each `x`, use the best odd remainder unless it equals `x`, otherwise use the second best.

## Approach

<!-- Describe your solution approach here -->
