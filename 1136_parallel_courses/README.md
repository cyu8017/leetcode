# 1136. Parallel Courses

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/parallel-courses/](https://leetcode.com/problems/parallel-courses/)
- **Premium:** Yes
- **Tags:** graph-theory, topological-sort

## Problem

You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given an array `relations` where `relations[i] = [prevCourse_{i}, nextCourse_{i}]`, representing a prerequisite relationship between course `prevCourse_{i}` and course `nextCourse_{i}`: course `prevCourse_{i}` has to be taken before course `nextCourse_{i}`.

In one semester, you can take **any number** of courses as long as you have taken all the prerequisites in the **previous** semester for the courses you are taking.

Return *the **minimum** number of semesters needed to take all courses*. If there is no way to take all the courses, return `-1`.



**Example 1:**

**Input:** n = 3, relations = [[1,3],[2,3]]
**Output:** 2
**Explanation:** The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.

**Example 2:**

**Input:** n = 3, relations = [[1,2],[2,3],[3,1]]
**Output:** -1
**Explanation:** No course can be studied because they are prerequisites of each other.



**Constraints:**

	- `1 <= n <= 5000`

	- `1 <= relations.length <= 5000`

	- `relations[i].length == 2`

	- `1 <= prevCourse_{i}, nextCourse_{i} <= n`

	- `prevCourse_{i} != nextCourse_{i}`

	- All the pairs `[prevCourse_{i}, nextCourse_{i}]` are **unique**.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Try to think of it as a graph problem. It will be impossible to study all the courses if the graph had a cycle.
2. The graph is a directed acyclic graph (DAG). The answer is the longes path in this DAG.
3. You can use DP to find the longest path in the DAG.

## Approach

<!-- Describe your solution approach here -->
