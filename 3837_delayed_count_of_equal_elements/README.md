# 3837. Delayed Count of Equal Elements

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/delayed-count-of-equal-elements/](https://leetcode.com/problems/delayed-count-of-equal-elements/)
- **Premium:** Yes
- **Tags:** array, hash-table, counting

## Problem

You are given an integer array `nums` of length `n` and an integer `k`.

For each index `i`, define the **delayed count** as the number of indices `j` such that:

	- `i + k < j <= n - 1`, and

	- `nums[j] == nums[i]`

Return an array `ans` where `ans[i]` is the **delayed count** of index `i`.



**Example 1:**

**Input:** nums = [1,2,1,1], k = 1

**Output:** [2,0,0,0]

**Explanation:**



			`i`
			`nums[i]`
			possible `j`
			`nums[j]`
			satisfying

			`nums[j] == nums[i]`
			`ans[i]`




			0
			1
			[2, 3]
			[1, 1]
			[2, 3]
			2


			1
			2
			[3]
			[1]
			[]
			0


			2
			1
			[]
			[]
			[]
			0


			3
			1
			[]
			[]
			[]
			0



Thus, `ans = [2, 0, 0, 0]`​​​​​​​.

**Example 2:**

**Input:** nums = [3,1,3,1], k = 0

**Output:** [1,1,0,0]

**Explanation:**



			`i`
			`nums[i]`
			possible `j`
			`nums[j]`
			satisfying

			`nums[j] == nums[i]`
			`ans[i]`




			0
			3
			[1, 2, 3]
			[1, 3, 1]
			[2]
			1


			1
			1
			[2, 3]
			[3, 1]
			[3]
			1


			2
			3
			[3]
			[1]
			[]
			0


			3
			1
			[]
			[]
			[]
			0



Thus, `ans = [1, 1, 0, 0]`​​​​​​​.



**Constraints:**

	- `1 <= n == nums.length <= 10^{5}`

	- `1 <= nums[i] <= 10^{5}`

	- `0 <= k <= n - 1`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use a hashmap.
2. Traverse from left to right, and at index `i` insert `nums[i + k + 1]` (if it exists) into the hashmap.
3. For the current index `i`, count how many of its occurrences are in the hashmap and push it into the result.
4. Reverse the resulting list and return it.

## Approach

<!-- Describe your solution approach here -->
