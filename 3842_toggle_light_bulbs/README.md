# 3842. Toggle Light Bulbs

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/toggle-light-bulbs/](https://leetcode.com/problems/toggle-light-bulbs/)
- **Tags:** array, hash-table, sorting, simulation

## Problem

You are given an array `bulbs` of integers between 1 and 100.

There are 100 light bulbs numbered from 1 to 100. All of them are switched off initially.

For each element `bulbs[i]` in the array `bulbs`:

- If the `bulbs[i]^{th}` light bulb is currently off, switch it on.

	- Otherwise, switch it off.

Return the list of integers denoting the light bulbs that are on in the end, **sorted** in **ascending** order. If no bulb is on, return an empty list.

**Example 1:**

**Input:** bulbs = [10,30,20,10]

**Output:** [20,30]

**Explanation:**

- The `bulbs[0] = 10^{th}` light bulb is currently off. We switch it on.

	- The `bulbs[1] = 30^{th}` light bulb is currently off. We switch it on.

	- The `bulbs[2] = 20^{th}` light bulb is currently off. We switch it on.

	- The `bulbs[3] = 10^{th}` light bulb is currently on. We switch it off.

	- In the end, the 20^{th} and the 30^{th} light bulbs are on.

**Example 2:**

**Input:** bulbs = [100,100]

**Output:** []

**Explanation:**

- The `bulbs[0] = 100^{th}` light bulb is currently off. We switch it on.

	- The `bulbs[1] = 100^{th}` light bulb is currently on. We switch it off.

	- In the end, no light bulb is on.

**Constraints:**

- `1 <= bulbs.length <= 100`

	- `1 <= bulbs[i] <= 100`

### Hints

1. Simulate as described

## Approach

<!-- Describe your solution approach here -->
