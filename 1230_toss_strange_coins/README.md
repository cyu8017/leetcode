# 1230. Toss Strange Coins

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/toss-strange-coins/](https://leetcode.com/problems/toss-strange-coins/)
- **Premium:** Yes
- **Tags:** array, math, dynamic-programming, probability-and-statistics

## Problem

You have some coins.  The `i`-th coin has a probability `prob[i]` of facing heads when tossed.

Return the probability that the number of coins facing heads equals `target` if you toss every coin exactly once.



**Example 1:**

**Input:** prob = [0.4], target = 1
**Output:** 0.40000

**Example 2:**

**Input:** prob = [0.5,0.5,0.5,0.5,0.5], target = 0
**Output:** 0.03125



**Constraints:**

	- `1 <= prob.length <= 1000`

	- `0 <= prob[i] <= 1`

	- `0 <= target``<= prob.length`

	- Answers will be accepted as correct if they are within `10^-5` of the correct answer.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. What about solving the problem with DP?
2. Use DP with two states dp[pos][cnt], where pos represents the pos-th coin and cnt is the number of heads seen so far.
3. You can do the transitions with a little bit math.
4. For the base case, when pos == n return (cnt == target) to filter out the invalid scenarios.

## Approach

<!-- Describe your solution approach here -->
