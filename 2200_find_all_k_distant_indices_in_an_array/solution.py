# LeetCode 2200 - Find All K-Distant Indices in an Array
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

from typing import List
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        mark = [False] * (n)
        for i in range(n):
            if nums[i] == key:
                l = max(0, i - k)
                r = min(n - 1, i + k)
                for j in range(l, (r) + 1):
                    mark[j] = True
        ans = []
        for i in range(n):
            if mark[i]:
                ans.append(i)
        return ans
