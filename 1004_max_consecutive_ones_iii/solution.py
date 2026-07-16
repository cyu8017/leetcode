# LeetCode 1004 - Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = zeros = ans = 0
        for right, x in enumerate(nums):
            zeros += x == 0
            while zeros > k:
                zeros -= nums[left] == 0
                left += 1
            ans = max(ans, right - left + 1)
        return ans
