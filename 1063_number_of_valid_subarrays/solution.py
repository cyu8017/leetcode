# LeetCode 1063 - Number of Valid Subarrays
# https://leetcode.com/problems/number-of-valid-subarrays/

class Solution:
    def validSubarrays(self, nums: list[int]) -> int:
        stack: list[int] = []
        ans = 0
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] > x:
                j = stack.pop()
                ans += i - j
            stack.append(i)
        while stack:
            j = stack.pop()
            ans += len(nums) - j
        return ans
