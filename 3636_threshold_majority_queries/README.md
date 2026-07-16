# 3636. Threshold Majority Queries

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/threshold-majority-queries/](https://leetcode.com/problems/threshold-majority-queries/)
- **Tags:** array, hash-table, binary-search, divide-and-conquer, counting, prefix-sum

## Problem

You are given an integer array `nums` of length `n` and an array `queries`, where `queries[i] = [l_{i}, r_{i}, threshold_{i}]`.

Return an array of integers ans where ans[i] is equal to the element in the subarray nums[l_{i}...r_{i}] that appears **at least** threshold_{i} times, selecting the element with the **highest** frequency (choosing the **smallest** in case of a tie), or -1 if no such element *exists*.

**Example 1:**

**Input:** nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]]

**Output:** [1,-1,2]

**Explanation:**



			Query
			Sub-array
			Threshold
			Frequency table
			Answer




			[0, 5, 4]
			[1, 1, 2, 2, 1, 1]
			4
			1 → 4, 2 → 2
			1


			[0, 3, 3]
			[1, 1, 2, 2]
			3
			1 → 2, 2 → 2
			-1


			[2, 3, 2]
			[2, 2]
			2
			2 → 2
			2



**Example 2:**

**Input:** nums = [3,2,3,2,3,2,3], queries = [[0,6,4],[1,5,2],[2,4,1],[3,3,1]]

**Output:** [3,2,3,2]

**Explanation:**



			Query
			Sub-array
			Threshold
			Frequency table
			Answer




			[0, 6, 4]
			[3, 2, 3, 2, 3, 2, 3]
			4
			3 → 4, 2 → 3
			3


			[1, 5, 2]
			[2, 3, 2, 3, 2]
			2
			2 → 3, 3 → 2
			2


			[2, 4, 1]
			[3, 2, 3]
			1
			3 → 2, 2 → 1
			3


			[3, 3, 1]
			[2]
			1
			2 → 1
			2



**Constraints:**

1

	1

	1

	queries[i] = [l_{i}, r_{i}, threshold_{i}]

	0

	1

### Hints

1. Use sqrt decomposition: let `B = int(sqrt(n))` and sort queries by `(l//B, r)`
2. Maintain window `[L,R]` with a frequency map `cnt` and buckets `bucket[f]` of values at count `f`
3. Slide `L` and `R` per query, updating `cnt` and `bucket`, then scan from `threshold` to max freq to find the smallest valid value or -1

## Approach

<!-- Describe your solution approach here -->
