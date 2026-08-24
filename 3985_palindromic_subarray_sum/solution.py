# LeetCode 3985 - Palindromic Subarray Sum
# https://leetcode.com/problems/palindromic-subarray-sum/

from typing import List


class Solution:
    def maxPalindromicSubarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        odd = [0] * n
        left = 0
        right = -1
        for i in range(n):
            radius = 1
            if i <= right:
                mirror = left + right - i
                radius = odd[mirror]
                if right - i + 1 < radius:
                    radius = right - i + 1
            while i - radius >= 0 and i + radius < n and nums[i - radius] == nums[i + radius]:
                radius += 1
            odd[i] = radius
            if i + radius - 1 > right:
                left = i - radius + 1
                right = i + radius - 1
        even = [0] * n
        left = 0
        right = -1
        for i in range(n):
            radius = 0
            if i <= right:
                mirror = left + right - i + 1
                radius = even[mirror]
                if right - i + 1 < radius:
                    radius = right - i + 1
            while i - radius - 1 >= 0 and i + radius < n and nums[i - radius - 1] == nums[i + radius]:
                radius += 1
            even[i] = radius
            if i + radius - 1 > right:
                left = i - radius
                right = i + radius - 1
        answer = 0
        for i in range(n):
            s = prefix[i + odd[i]] - prefix[i - odd[i] + 1]
            if s > answer:
                answer = s
            if even[i] > 0:
                s = prefix[i + even[i]] - prefix[i - even[i]]
                if s > answer:
                    answer = s
        return answer
