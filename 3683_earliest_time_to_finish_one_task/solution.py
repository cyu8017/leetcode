# LeetCode 3683 - Earliest Time to Finish One Task
# https://leetcode.com/problems/earliest-time-to-finish-one-task/

from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = 200
        for task in tasks:
            ans = min(ans, task[0] + task[1])
        return ans
