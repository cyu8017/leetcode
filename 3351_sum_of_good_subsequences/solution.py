# LeetCode 3351 - Sum of Good Subsequences
# https://leetcode.com/problems/sum-of-good-subsequences/

from typing import List


class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        mod = 1000000007
        cnt = {}
        ssum = {}
        ans = 0
        for x in nums:
            c = 1
            s = x
            if cnt.get(x - 1, 0) > 0:
                c = (c + cnt[x - 1]) % mod
                s = (s + ssum[x - 1] + cnt[x - 1] * x % mod) % mod
            if cnt.get(x + 1, 0) > 0:
                c = (c + cnt[x + 1]) % mod
                s = (s + ssum[x + 1] + cnt[x + 1] * x % mod) % mod
            cnt[x] = (cnt.get(x, 0) + c) % mod
            ssum[x] = (ssum.get(x, 0) + s) % mod
            ans = (ans + s) % mod
        return ans
