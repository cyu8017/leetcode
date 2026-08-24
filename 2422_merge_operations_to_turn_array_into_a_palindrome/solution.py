# LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
# https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        left, right = nums[l], nums[r]
        ans = 0
        while l < r:
            if left == right:
                l += 1
                r -= 1
                if l < r:
                    left = nums[l]
                    right = nums[r]
            elif left < right:
                l += 1
                left += nums[l]
                ans += 1
            else:
                r -= 1
                right += nums[r]
                ans += 1
        return ans
