from typing import List, Optional

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = zeros = ans = 0
        for right, x in enumerate(nums):
            zeros += x == 0
            while zeros > 1:
                zeros -= nums[left] == 0; left += 1
            ans = max(ans, right - left)
        return ans
