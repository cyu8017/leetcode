# LeetCode 2113 - Elements in Array After Removing and Replacing Elements
# https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

from typing import List
class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = [None] * (len(queries))
        for i in range(len(queries)):
            t = queries[i][0]
            idx = queries[i][1]
            cycle = t % (2 * n)
            size = None
            offset = None
            if cycle < n:
                size = n - cycle
                offset = cycle
            else:
                size = cycle - n
                offset = 0
            ans[i] = -1 if idx >= size else nums[offset + idx]
        return ans
