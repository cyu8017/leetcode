# LeetCode 1856 - Maximum Subarray Min-Product
# https://leetcode.com/problems/maximum-subarray-min-product/

from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for index, value in enumerate(nums):
            prefix[index + 1] = prefix[index] + value

        left_bound = [-1] * n
        stack: list[int] = []
        for index, value in enumerate(nums):
            while stack and nums[stack[-1]] >= value:
                stack.pop()
            left_bound[index] = stack[-1] if stack else -1
            stack.append(index)

        right_bound = [n] * n
        stack.clear()
        for index in range(n - 1, -1, -1):
            value = nums[index]
            while stack and nums[stack[-1]] >= value:
                stack.pop()
            right_bound[index] = stack[-1] if stack else n
            stack.append(index)

        best = 0
        for index, value in enumerate(nums):
            total = prefix[right_bound[index]] - prefix[left_bound[index] + 1]
            best = max(best, total * value)

        return best % mod
