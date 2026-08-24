# LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        INF = 9007199254740991
        best = [INF] * k
        best[0] = 0
        ans = -INF
        for i in range(1, n + 1):
            r = i % k
            if best[r] != INF:
                cand = pref[i] - best[r]
                if cand > ans:
                    ans = cand
            if pref[i] < best[r]:
                best[r] = pref[i]
        return ans
