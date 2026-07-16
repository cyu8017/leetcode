# 1773. Count Items Matching a Rule

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/count-items-matching-a-rule/](https://leetcode.com/problems/count-items-matching-a-rule/)
- **Tags:** array, string

## Problem

You are given an array `items`, where each `items[i] = [type_{i}, color_{i}, name_{i}]` describes the type, color, and name of the `i^{th}` item. You are also given a rule represented by two strings, `ruleKey` and `ruleValue`.

The `i^{th}` item is said to match the rule if **one** of the following is true:

- `ruleKey == "type"` and `ruleValue == type_{i}`.

	- `ruleKey == "color"` and `ruleValue == color_{i}`.

	- `ruleKey == "name"` and `ruleValue == name_{i}`.

Return *the number of items that match the given rule*.

**Example 1:**

```
**Input:** items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
**Output:** 1
**Explanation:** There is only one item matching the given rule, which is ["computer","silver","lenovo"].
```

**Example 2:**

```
**Input:** items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
**Output:** 2
**Explanation:** There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
```

**Constraints:**

- `1 <= items.length <= 10^{4}`

	- `1 <= type_{i}.length, color_{i}.length, name_{i}.length, ruleValue.length <= 10`

	- `ruleKey` is equal to either `"type"`, `"color"`, or `"name"`.

	- All strings consist only of lowercase letters.

### Hints

1. Iterate on each item, and check if each one matches the rule according to the statement.

## Approach

<!-- Describe your solution approach here -->
