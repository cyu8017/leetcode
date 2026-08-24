# LeetCode 3878 - Count Good Subarrays
# https://leetcode.com/problems/count-good-subarrays/

from typing import List


class Solution:
    def countGoodSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        l = [-1] * n
        stk: List[int] = []
        for i in range(n):
            x = nums[i]
            while stk and nums[stk[-1]] < x and (nums[stk[-1]] | x) == x:
                stk.pop()
            if stk:
                l[i] = stk[-1]
            stk.append(i)
        r = [n] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and (nums[stk[-1]] | nums[i]) == nums[i]:
                stk.pop()
            if stk:
                r[i] = stk[-1]
            stk.append(i)
        ans = 0
        for i in range(n):
            ans += (i - l[i]) * (r[i] - i)
        return ans
