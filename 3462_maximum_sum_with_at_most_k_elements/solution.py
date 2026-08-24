# LeetCode 3462 - Maximum Sum With at Most K Elements
# https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        h: List[int] = []
        s = 0

        def push(v: int) -> None:
            h.append(v)
            h.sort()

        def poll() -> int:
            return h.pop(0)

        for i in range(len(grid)):
            r = sorted(grid[i])
            lim = limits[i]
            if lim > len(r):
                lim = len(r)
            for j in range(lim):
                val = r[len(r) - 1 - j]
                push(val)
                s += val
                if len(h) > k:
                    s -= poll()
        return s
