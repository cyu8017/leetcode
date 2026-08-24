# LeetCode 2562 - Find the Array Concatenation Value
# https://leetcode.com/problems/find-the-array-concatenation-value/

from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                ans += nums[l]
                break
            left, right = nums[l], nums[r]
            p = 1
            t = right
            while t > 0:
                p *= 10
                t //= 10
            ans += left * p + right
            l += 1
            r -= 1
        return ans
