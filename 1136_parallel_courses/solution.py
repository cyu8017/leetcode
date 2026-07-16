# LeetCode 1136 - Parallel Courses
# https://leetcode.com/problems/parallel-courses/

from collections import deque


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)
        for prev, nxt in relations:
            graph[prev].append(nxt)
            indegree[nxt] += 1
        queue = deque(i for i in range(1, n + 1) if indegree[i] == 0)
        semesters = 0
        taken = 0
        while queue:
            semesters += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                taken += 1
                for nxt in graph[course]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)
        return semesters if taken == n else -1
