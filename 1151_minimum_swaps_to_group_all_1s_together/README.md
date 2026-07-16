# 1151. Minimum Swaps to Group All 1's Together

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/)
- **Premium:** Yes
- **Tags:** array, sliding-window

## Problem

Given a binary array `data`, return the minimum number of swaps required to group all `1`’s present in the array together in **any place** in the array.



**Example 1:**

**Input:** data = [1,0,1,0,1]
**Output:** 1
**Explanation:** There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.

**Example 2:**

**Input:** data = [0,0,0,1,0]
**Output:** 0
**Explanation:** Since there is only one 1 in the array, no swaps are needed.

**Example 3:**

**Input:** data = [1,0,1,0,1,0,0,1,1,0,1]
**Output:** 3
**Explanation:** One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].



**Constraints:**

	- `1 <= data.length <= 10^{5}`

	- `data[i]` is either `0` or `1`.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. How many 1's should be grouped together ? Is not a fixed number?
2. Yeah it's just the number of 1's the whole array has. Let's name this number as ones
3. Every subarray of size of ones, needs some number of swaps to reach, Can you find the number of swaps needed to group all 1's in this subarray?
4. It's the number of zeros in that subarray.
5. Do you need to count the number of zeros all over again for every position ?
6. Use Sliding Window technique.

## Approach

<!-- Describe your solution approach here -->
