# LeetCode 3364 - Minimum Positive Sum Subarray
# https://leetcode.com/problems/minimum-positive-sum-subarray/

from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        ans = 2147483647
        found = False
        for i in range(n):
            length = l
            while length <= r and i + length <= n:
                s = pref[i + length] - pref[i]
                if s > 0 and s < ans:
                    ans = s
                    found = True
                length += 1
        return ans if found else -1
