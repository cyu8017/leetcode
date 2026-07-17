# LeetCode 1834 - Single-Threaded CPU
# https://leetcode.com/problems/single-threaded-cpu/

import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        indexed = sorted(enumerate(tasks), key=lambda item: (item[1][0], item[0]))
        i = 0
        n = len(tasks)
        heap: list[tuple[int, int]] = []
        time = 0
        order: list[int] = []

        while i < n or heap:
            if i < n and not heap:
                time = max(time, indexed[i][1][0])

            while i < n and indexed[i][1][0] <= time:
                idx, task = indexed[i]
                heapq.heappush(heap, (task[1], idx))
                i += 1

            duration, idx = heapq.heappop(heap)
            time += duration
            order.append(idx)

        return order
