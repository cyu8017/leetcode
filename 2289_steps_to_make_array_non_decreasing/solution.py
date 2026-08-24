# LeetCode 2289 - Steps to Make Array Non-decreasing
# https://leetcode.com/problems/steps-to-make-array-non-decreasing/

from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            steps = 0
            while stack and nums[i] > stack[-1][0]:
                steps = max(steps, stack[-1][1])
                stack.pop()
                steps += 1
            ans = max(ans, steps)
            stack.append((nums[i], steps))
        return ans
