# LeetCode 3152 - Special Array II
# https://leetcode.com/problems/special-array-ii/

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        d = list(range(n))
        for i in range(1, n):
            if nums[i] % 2 != nums[i - 1] % 2:
                d[i] = d[i - 1]
        ans = [False] * len(queries)
        for i, q in enumerate(queries):
            ans[i] = d[q[1]] <= q[0]
        return ans
