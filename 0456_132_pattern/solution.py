# LeetCode 0456 - 132 Pattern
# https://leetcode.com/problems/132-pattern/


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack: list[int] = []
        third = float("-inf")
        for value in reversed(nums):
            if value < third:
                return True
            while stack and value > stack[-1]:
                third = stack.pop()
            stack.append(value)
        return False
