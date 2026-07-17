# LeetCode 1838 - Frequency of the Most Frequent Element
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        best = 0

        for right, value in enumerate(nums):
            window_sum += value
            while value * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            best = max(best, right - left + 1)

        return best
