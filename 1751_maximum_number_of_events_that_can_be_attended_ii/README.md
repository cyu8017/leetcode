# 1751. Maximum Number of Events That Can Be Attended II

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/)
- **Tags:** array, binary-search, dynamic-programming, sorting

## Problem

You are given an array of `events` where `events[i] = [startDay_{i}, endDay_{i}, value_{i}]`. The `i^{th}` event starts at `startDay_{i}`_{ }and ends at `endDay_{i}`, and if you attend this event, you will receive a value of `value_{i}`. You are also given an integer `k` which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the **entire** event. Note that the end day is **inclusive**: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return *the **maximum sum** of values that you can receive by attending events.*

**Example 1:**

```
**Input:** events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
**Output:** 7
**Explanation: **Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
```

**Example 2:**

```
**Input:** events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
**Output:** 10
**Explanation:** Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do **not** have to attend k events.
```

**Example 3:**

**

```
**Input:** events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
**Output:** 9
**Explanation:** Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
```

**Constraints:**

- `1 <= k <= events.length`

	- `1 <= k * events.length <= 10^{6}`

	- `1 <= startDay_{i} <= endDay_{i} <= 10^{9}`

	- `1 <= value_{i} <= 10^{6}`

### Hints

1. Sort the events by its startTime.
2. For every event, you can either choose it and consider the next event available, or you can ignore it. You can efficiently find the next event that is available using binary search.

## Approach

<!-- Describe your solution approach here -->
