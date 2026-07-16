# 2548. Maximum Price to Fill a Bag

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/maximum-price-to-fill-a-bag/](https://leetcode.com/problems/maximum-price-to-fill-a-bag/)
- **Premium:** Yes
- **Tags:** array, greedy, sorting

## Problem

You are given a 2D integer array `items` where `items[i] = [price_{i}, weight_{i}]` denotes the price and weight of the `i^{th}` item, respectively.

You are also given a **positive** integer `capacity`.

Each item can be divided into two items with ratios `part1` and `part2`, where `part1 + part2 == 1`.

	- The weight of the first item is `weight_{i} * part1` and the price of the first item is `price_{i} * part1`.

	- Similarly, the weight of the second item is `weight_{i} * part2` and the price of the second item is `price_{i} * part2`.

Return ***the maximum total price** to fill a bag of capacity* `capacity` *with given items*. If it is impossible to fill a bag return `-1`. Answers within `10^{-5}` of the **actual answer** will be considered accepted.



**Example 1:**

**Input:** items = [[50,1],[10,8]], capacity = 5
**Output:** 55.00000
**Explanation:**
We divide the 2^{nd} item into two parts with part1 = 0.5 and part2 = 0.5.
The price and weight of the 1^{st} item are 5, 4. And similarly, the price and the weight of the 2^{nd} item are 5, 4.
The array items after operation becomes [[50,1],[5,4],[5,4]].
To fill a bag with capacity 5 we take the 1^{st} element with a price of 50 and the 2^{nd} element with a price of 5.
It can be proved that 55.0 is the maximum total price that we can achieve.

**Example 2:**

**Input:** items = [[100,30]], capacity = 50
**Output:** -1.00000
**Explanation:** It is impossible to fill a bag with the given item.



**Constraints:**

	- `1 <= items.length <= 10^{5}`

	- `items[i].length == 2`

	- `1 <= price_{i}, weight_{i} <= 10^{4}`

	- `1 <= capacity <= 10^{9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. If the total weight of the items is less than the capacity, then it is impossible to fill a bag.
2. The intended solution greedily chooses items to fill a bag.
3. Sort items in decreasing order of price/weight and greedily fill a bag. The main intuition behind the greedy strategy is that we try to take the highest possible price for 1 unit of weight.

## Approach

<!-- Describe your solution approach here -->
