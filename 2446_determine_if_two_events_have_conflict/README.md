# 2446. Determine if Two Events Have Conflict

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/determine-if-two-events-have-conflict/](https://leetcode.com/problems/determine-if-two-events-have-conflict/)
- **Tags:** array, string

## Problem

You are given two arrays of strings that represent two inclusive events that happened **on the same day**, `event1` and `event2`, where:

- `event1 = [startTime_{1}, endTime_{1}]` and

	- `event2 = [startTime_{2}, endTime_{2}]`.

Event times are valid 24 hours format in the form of `HH:MM`.

A **conflict** happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return `true`* if there is a conflict between two events. Otherwise, return *`false`.

**Example 1:**

```
**Input:** event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
**Output:** true
**Explanation:** The two events intersect at time 2:00.
```

**Example 2:**

```
**Input:** event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
**Output:** true
**Explanation:** The two events intersect starting from 01:20 to 02:00.
```

**Example 3:**

```
**Input:** event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
**Output:** false
**Explanation:** The two events do not intersect.
```

**Constraints:**

- `event1.length == event2.length == 2`

	- `event1[i].length == event2[i].length == 5`

	- `startTime_{1} <= endTime_{1}`

	- `startTime_{2} <= endTime_{2}`

	- All the event times follow the `HH:MM` format.

### Hints

1. Parse time format to some integer interval first
2. How would you determine if two intervals overlap?

## Approach

<!-- Describe your solution approach here -->
