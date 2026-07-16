# 0210. Course Schedule II

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/course-schedule-ii/](https://leetcode.com/problems/course-schedule-ii/)
- **Tags:** depth-first-search, breadth-first-search, graph-theory, topological-sort

## Problem

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_{i}, b_{i}]` indicates that you **must** take course `b_{i}` first if you want to take course `a_{i}`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return *the ordering of courses you should take to finish all courses*. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

**Example 1:**

```
**Input:** numCourses = 2, prerequisites = [[1,0]]
**Output:** [0,1]
**Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

**Example 2:**

```
**Input:** numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
**Output:** [0,2,1,3]
**Explanation:** There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```

**Example 3:**

```
**Input:** numCourses = 1, prerequisites = []
**Output:** [0]
```

**Constraints:**

- `1 <= numCourses <= 2000`

	- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`

	- `prerequisites[i].length == 2`

	- `0 <= a_{i}, b_{i} < numCourses`

	- `a_{i} != b_{i}`

	- All the pairs `[a_{i}, b_{i}]` are **distinct**.

### Hints

1. This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
2. [Topological Sort via DFS](https://www.youtube.com/watch?v=ozso3xxkVGU) - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
3. Topological sort could also be done via [BFS](http://en.wikipedia.org/wiki/Topological_sorting#Algorithms).

## Approach

<!-- Describe your solution approach here -->
