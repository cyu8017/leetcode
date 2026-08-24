# LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

from typing import List


class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            mn = mx = nums[i]
            j = i
            while j < n and j - i + 1 <= k:
                if nums[j] < mn:
                    mn = nums[j]
                if nums[j] > mx:
                    mx = nums[j]
                ans += mn + mx
                j += 1
        return ans
