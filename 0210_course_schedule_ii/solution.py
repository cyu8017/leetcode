# LeetCode 0210 - Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph: dict[int, list[int]] = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order: list[int] = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return order if len(order) == numCourses else []
