# LeetCode 0503 - Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = [-1] * length
        stack: list[int] = []
        for index in range(length * 2):
            while stack and nums[stack[-1]] < nums[index % length]:
                result[stack.pop()] = nums[index % length]
            if index < length:
                stack.append(index)
        return result
