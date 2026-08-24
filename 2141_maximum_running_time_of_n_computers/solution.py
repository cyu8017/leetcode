# LeetCode 2141 - Maximum Running Time of N Computers
# https://leetcode.com/problems/maximum-running-time-of-n-computers/

from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        sum = 0
        for b in batteries:
            sum += b
        lo = 1
        hi = sum // n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            need = 0
            for b in batteries:
                need += min(b, mid)
            if need >= mid * n:
                lo = mid
            else:
                hi = mid - 1
        return lo
