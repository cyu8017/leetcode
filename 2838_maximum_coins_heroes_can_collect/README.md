# 2838. Maximum Coins Heroes Can Collect

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/maximum-coins-heroes-can-collect/](https://leetcode.com/problems/maximum-coins-heroes-can-collect/)
- **Premium:** Yes
- **Tags:** array, two-pointers, binary-search, sorting, prefix-sum

## Problem

There is a battle and `n` heroes are trying to defeat `m` monsters. You are given two **1-indexed** arrays of **positive** integers `heroes` and `monsters` of length `n` and `m`, respectively. `heroes[i]` is the power of `i^{th}` hero, and `monsters[i]` is the power of `i^{th}` monster.

The `i^{th}` hero can defeat the `j^{th}` monster if `monsters[j] <= heroes[i]`.

You are also given a **1-indexed** array `coins` of length `m` consisting of **positive** integers. `coins[i]` is the number of coins that each hero earns after defeating the `i^{th}` monster.

Return* an array *`ans`* of length *`n`* where *`ans[i]`* is the **maximum** number of coins that the *`i^{th}`* hero can collect from this battle*.

**Notes**

	- The health of a hero doesn't get reduced after defeating a monster.

	- Multiple heroes can defeat a monster, but each monster can be defeated by a given hero only once.



**Example 1:**

**Input:** heroes = [1,4,2], monsters = [1,1,5,2,3], coins = [2,3,4,5,6]
**Output:** [5,16,10]
**Explanation: **For each hero, we list the index of all the monsters he can defeat:
1^{st} hero: [1,2] since the power of this hero is 1 and monsters[1], monsters[2]

**Example 2:**

**Input:** heroes = [5], monsters = [2,3,1,2], coins = [10,6,5,2]
**Output:** [23]
**Explanation:** This hero can defeat all the monsters since monsters[i]

**Example 3:**

**Input:** heroes = [4,4], monsters = [5,7,8], coins = [1,1,1]
**Output:** [0,0]
**Explanation:** In this example, no hero can defeat a monster. So the answer would be [0,0],



**Constraints:**

	- `1 <= n == heroes.length <= 10^{5}`

	- `1 <= m == monsters.length <= 10^{5}`

	- `coins.length == m`

	- `1 <= heroes[i], monsters[i], coins[i] <= 10^{9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. If a hero can defeat the `i^{th}` monster, then he defeats all the monsters having a power less than `monster[i]`.
2. Sort monsters by their powers. Also change the order of the coins array according to this sort.
3. Construct a prefix sum array for the updated coins array.
4. For each hero, do a binary search and find the last position of the most powerful monster that this hero can defeat.
5. If said monster has index `i`, then the `i^{th}` element of the partial sum array would be the answer.

## Approach

<!-- Describe your solution approach here -->
