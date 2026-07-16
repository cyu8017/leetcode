# 0253. Meeting Rooms II

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/meeting-rooms-ii/](https://leetcode.com/problems/meeting-rooms-ii/)
- **Premium:** Yes
- **Tags:** array, two-pointers, greedy, sorting, heap-(priority-queue), prefix-sum

## Problem

Given an array of meeting time intervals `intervals` where `intervals[i] = [start_{i}, end_{i}]`, return *the minimum number of conference rooms required*.



**Example 1:**

**Input:** intervals = [[0,30],[5,10],[15,20]]
**Output:** 2

**Example 2:**

**Input:** intervals = [[7,10],[2,4]]
**Output:** 1



**Constraints:**

	- `1 <= intervals.length <= 10^{4}`

	- `0 <= start_{i} < end_{i} <= 10^{6}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Think about how we would approach this problem in a very simplistic way. We will allocate rooms to meetings that occur earlier in the day v/s the ones that occur later on, right?
2. If you've figured out that we have to **sort** the meetings by their start time, the next thing to think about is how do we do the allocation?
There are two scenarios possible here for any meeting. Either there is no meeting room available and a new one has to be allocated, or a meeting room has freed up and this meeting can take place there.
3. An important thing to note is that we don't really care **which** room gets freed up while allocating a room for the current meeting. As long as a room is free, our job is done.

We already know the rooms we have allocated till now and we also know when are they due to get free because of the end times of the meetings going on in those rooms. We can simply check the room which is due to get vacated the earliest amongst all the allocated rooms.
4. Following up on the previous hint, we can make use of a min-heap to store the end times of the meetings in various rooms.

So, every time we want to check if any room is free or not, simply check the topmost element of the min heap as that would be the room that would get free the earliest out of all the other rooms currently occupied.

If the room we extracted from the top of the min heap isn't free, then no other room is. So, we can save time here and simply allocate a new room.

## Approach

<!-- Describe your solution approach here -->
