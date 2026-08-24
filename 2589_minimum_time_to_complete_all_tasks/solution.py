# LeetCode 2589 - Minimum Time to Complete All Tasks
# https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1])
        on = [False] * 2001
        ans = 0
        for start, end, dur in tasks:
            have = 0
            for i in range(start, end + 1):
                if on[i]:
                    have += 1
            need = dur - have
            i = end
            while i >= start and need > 0:
                if not on[i]:
                    on[i] = True
                    need -= 1
                    ans += 1
                i -= 1
        return ans
