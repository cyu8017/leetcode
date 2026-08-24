# LeetCode 3026 - Maximum Good Subarray Sum
# https://leetcode.com/problems/maximum-good-subarray-sum/

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        p = {}
        p[nums[0]] = 0
        s = 0
        n = len(nums)
        ans = float("-inf")
        for i in range(n):
            s += nums[i]
            if nums[i] - k in p:
                ans = max(ans, s - p[nums[i] - k])
            if nums[i] + k in p:
                ans = max(ans, s - p[nums[i] + k])
            if i + 1 == n:
                break
            old = p.get(nums[i + 1])
            if old is None or s < old:
                p[nums[i + 1]] = s
        return 0 if ans == float("-inf") else ans
