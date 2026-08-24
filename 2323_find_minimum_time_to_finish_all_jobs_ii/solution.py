# LeetCode 2323 - Find Minimum Time to Finish All Jobs II
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

from typing import List


class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        ans = 0
        for i in range(len(jobs)):
            ans = max(ans, (jobs[i] + workers[i] - 1) // workers[i])
        return ans
