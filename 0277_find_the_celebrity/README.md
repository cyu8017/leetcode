# 0277. Find the Celebrity

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/find-the-celebrity/](https://leetcode.com/problems/find-the-celebrity/)
- **Premium:** Yes
- **Tags:** two-pointers, graph-theory, interactive

## Problem

Suppose you are at a party with `n` people labeled from `0` to `n - 1` and among them, there may exist one celebrity. The definition of a celebrity is that all the other `n - 1` people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given an integer `n` and a helper function `bool knows(a, b)` that tells you whether `a` knows `b`. Implement a function `int findCelebrity(n)`. There will be exactly one celebrity if they are at the party.

Return *the celebrity's label if there is a celebrity at the party*. If there is no celebrity, return `-1`.

**Note** that the `n x n` 2D array `graph` given as input is **not** directly available to you, and instead **only** accessible through the helper function `knows`. `graph[i][j] == 1` represents person `i` knows person `j`, wherease `graph[i][j] == 0` represents person `j` does not know person `i`.



**Example 1:**

**Input:** graph = [[1,1,0],[0,1,0],[1,1,1]]
**Output:** 1
**Explanation:** There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

**Example 2:**

**Input:** graph = [[1,0,1],[1,1,0],[0,1,1]]
**Output:** -1
**Explanation:** There is no celebrity.



**Constraints:**

	- `n == graph.length == graph[i].length`

	- `2 <= n <= 100`

	- `graph[i][j]` is `0` or `1`.

	- `graph[i][i] == 1`



**Follow up:** If the maximum number of allowed calls to the API `knows` is `3 * n`, could you find a solution without exceeding the maximum number of calls?

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. The best hint for this problem can be provided by the following figure:
2. Well, if you understood the gist of the above idea, you can extend it to find a candidate that can possibly be a celebrity. Why do we say a "candidate"? That is for you to think. This is clearly a greedy approach to find the answer. However, there is some information that would still remain to be verified without which we can't obtain an answer with certainty. To get that stake in the ground, we would need some more calls to the knows API.

## Approach

<!-- Describe your solution approach here -->
