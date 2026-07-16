# 2247. Maximum Cost of Trip With K Highways

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/](https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/)
- **Premium:** Yes
- **Tags:** dynamic-programming, bit-manipulation, graph-theory, bitmask

## Problem

A series of highways connect `n` cities numbered from `0` to `n - 1`. You are given a 2D integer array `highways` where `highways[i] = [city1_{i}, city2_{i}, toll_{i}]` indicates that there is a highway that connects `city1_{i}` and `city2_{i}`, allowing a car to go from `city1_{i}` to `city2_{i}` and **vice versa** for a cost of `toll_{i}`.

You are also given an integer `k`. You are going on a trip that crosses **exactly** `k` highways. You may start at any city, but you may only visit each city **at most** once during your trip.

Return* the **maximum** cost of your trip. If there is no trip that meets the requirements, return *`-1`*.*



**Example 1:**

**Input:** n = 5, highways = [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]], k = 3
**Output:** 17
**Explanation:**
One possible trip is to go from 0 -> 1 -> 4 -> 3. The cost of this trip is 4 + 11 + 2 = 17.
Another possible trip is to go from 4 -> 1 -> 2 -> 3. The cost of this trip is 11 + 3 + 3 = 17.
It can be proven that 17 is the maximum possible cost of any valid trip.

Note that the trip 4 -> 1 -> 0 -> 1 is not allowed because you visit the city 1 twice.

**Example 2:**

**Input:** n = 4, highways = [[0,1,3],[2,3,2]], k = 2
**Output:** -1
**Explanation:** There are no valid trips of length 2, so return -1.



**Constraints:**

	- `2 <= n <= 15`

	- `1 <= highways.length <= 50`

	- `highways[i].length == 3`

	- `0 <= city1_{i}, city2_{i} <= n - 1`

	- `city1_{i} != city2_{i}`

	- `0 <= toll_{i} <= 100`

	- `1 <= k <= 50`

	- There are no duplicate highways.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Are there any computations being repeated?
2. The same path can be visited multiple times. Could we reuse the previously calculated result?
3. Store the nodes seen on the current path and the last node on the current path as a dynamic programming state.

## Approach

<!-- Describe your solution approach here -->
