# 2927. Distribute Candies Among Children III

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/distribute-candies-among-children-iii/](https://leetcode.com/problems/distribute-candies-among-children-iii/)
- **Premium:** Yes
- **Tags:** math, combinatorics

## Problem

You are given two positive integers `n` and `limit`.

Return *the **total number** of ways to distribute *`n` *candies among *`3`* children such that no child gets more than *`limit`* candies.*



**Example 1:**

**Input:** n = 5, limit = 2
**Output:** 3
**Explanation:** There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).

**Example 2:**

**Input:** n = 3, limit = 3
**Output:** 10
**Explanation:** There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).



**Constraints:**

	- `1 <= n <= 10^{8}`

	- `1 <= limit <= 10^{8}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Try to solve the problem using combinatorics.
2. If the limit didn’t exist, the problem would be distributing `n` candies between `3` children.
3. The answer to the above problem would be `C(n + 2, 2)`.
4. Now try to combine this with the Inclusion-exclusion principle.
5. Apart from the above solution, there are other mathematical solutions that you can think of.

## Approach

<!-- Describe your solution approach here -->
