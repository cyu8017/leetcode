# LeetCode 3676 - Count Bowl Subarrays
# https://leetcode.com/problems/count-bowl-subarrays/

from typing import List


class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        ngr = [-1] * n
        ngl = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                ngr[i] = stack[-1]
            stack.append(i)
        stack.clear()
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                ngl[i] = stack[-1]
            stack.append(i)
        for i in range(n):
            if ngr[i] != -1 and ngr[i] - i >= 2:
                ans += 1
            if ngl[i] != -1 and i - ngl[i] >= 2:
                ans += 1
        return ans
