# LeetCode 2537 - Count the Number of Good Subarrays
# https://leetcode.com/problems/count-the-number-of-good-subarrays/

from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = {}
        pairs = 0
        ans = 0
        left = 0
        for right in range(len(nums)):
            pairs += freq.get(nums[right], 0)
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while pairs >= k:
                ans += len(nums) - right
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1
        return ans
