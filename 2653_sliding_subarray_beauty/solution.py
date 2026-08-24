# LeetCode 2653 - Sliding Subarray Beauty
# https://leetcode.com/problems/sliding-subarray-beauty/

from typing import List


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = [0] * 101
        ans = [0] * (len(nums) - k + 1)
        for i, num in enumerate(nums):
            freq[num + 50] += 1
            if i >= k:
                freq[nums[i - k] + 50] -= 1
            if i >= k - 1:
                need, val = x, 0
                for j in range(50):
                    need -= freq[j]
                    if need <= 0:
                        val = j - 50
                        break
                ans[i - k + 1] = val
        return ans
