# LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
# https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = -1 if not stack else stack[-1]
            stack.append(i)
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = n if not stack else stack[-1]
            stack.append(i)
        for i in range(n):
            k = right[i] - left[i] - 1
            if nums[i] > threshold // k:
                return k
        return -1
