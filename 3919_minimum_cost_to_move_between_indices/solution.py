# LeetCode 3919 - Minimum Cost To Move Between Indices
# https://leetcode.com/problems/minimum-cost-to-move-between-indices/

from typing import List


class Solution:
    def minCost(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        s1 = [0] * n
        s2 = [0] * n
        for i in range(1, n):
            c1 = 1
            if i > 1 and nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1]:
                c1 = nums[i] - nums[i - 1]
            c2 = 1
            if i < n - 1 and nums[i] - nums[i - 1] > nums[i + 1] - nums[i]:
                c2 = nums[i] - nums[i - 1]
            s1[i] = s1[i - 1] + c1
            s2[i] = s2[i - 1] + c2
        ans = [0] * len(queries)
        for i in range(len(queries)):
            l, r = queries[i][0], queries[i][1]
            ans[i] = (s1[r] - s1[l]) if l < r else (s2[l] - s2[r])
        return ans
