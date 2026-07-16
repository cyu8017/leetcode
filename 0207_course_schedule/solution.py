# LeetCode 0207 - Course Schedule
# https://leetcode.com/problems/course-schedule/

from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: dict[int, list[int]] = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0
        while queue:
            node = queue.popleft()
            taken += 1
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return taken == numCourses
