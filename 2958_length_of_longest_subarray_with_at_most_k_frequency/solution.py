# LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        ans = 0
        left = 0
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            if right - left + 1 > ans:
                ans = right - left + 1
        return ans
