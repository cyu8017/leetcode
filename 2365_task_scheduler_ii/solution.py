# LeetCode 2365 - Task Scheduler II
# https://leetcode.com/problems/task-scheduler-ii/

from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        nxt = {}
        day = 0
        for t in tasks:
            day = max(day, nxt.get(t, 0))
            day += 1
            nxt[t] = day + space
        return day
