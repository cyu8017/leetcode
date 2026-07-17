# LeetCode 1882 - Process Tasks Using Servers
# https://leetcode.com/problems/process-tasks-using-servers/

import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(weight, index) for index, weight in enumerate(servers)]
        heapq.heapify(available)
        busy: list[tuple[int, int, int]] = []
        answer: List[int] = []
        time = 0

        for moment, task in enumerate(tasks):
            time = max(time, moment)
            while busy and busy[0][0] <= time:
                finish_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            while not available:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    finish_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)
            heapq.heappush(busy, (time + task, weight, index))
            answer.append(index)

        return answer
