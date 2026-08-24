# LeetCode 3488 - Closest Equal Element Queries
# https://leetcode.com/problems/closest-equal-element-queries/

from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = {}
        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = []
            pos[x].append(i)
        ans = [0] * len(queries)
        for qi, idx in enumerate(queries):
            x = nums[idx]
            arr = pos[x]
            if len(arr) == 1:
                ans[qi] = -1
                continue
            best = n
            for p in arr:
                if p == idx:
                    continue
                d = abs(p - idx)
                d = min(d, n - d)
                if d < best:
                    best = d
            ans[qi] = best
        return ans
