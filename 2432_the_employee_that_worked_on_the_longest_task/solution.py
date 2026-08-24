# LeetCode 2432 - The Employee That Worked on the Longest Task
# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans = logs[0][0]
        best = logs[0][1]
        prev = 0
        for emp, t in logs:
            dur = t - prev
            if dur > best or (dur == best and emp < ans):
                best = dur
                ans = emp
            prev = t
        return ans
