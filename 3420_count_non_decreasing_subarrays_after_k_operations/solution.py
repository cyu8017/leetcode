# LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

from typing import List


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            cost = 0
            max_v = nums[i]
            for j in range(i, n):
                if nums[j] >= max_v:
                    max_v = nums[j]
                else:
                    cost += max_v - nums[j]
                if cost > k:
                    break
                ans += 1
        return ans
