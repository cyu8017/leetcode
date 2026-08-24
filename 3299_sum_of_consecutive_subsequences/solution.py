# LeetCode 3299 - Sum of Consecutive Subsequences
# https://leetcode.com/problems/sum-of-consecutive-subsequences/

from typing import Dict, List


class Solution:
    def rangeSum(self, nums: List[int]) -> int:
        mod = 1000000007
        cnt: Dict[int, int] = {}
        sm: Dict[int, int] = {}
        ans = 0
        for x in nums:
            cL, sL = cnt.get(x - 1, 0), sm.get(x - 1, 0)
            cR, sR = cnt.get(x + 1, 0), sm.get(x + 1, 0)
            c = (1 + cL + cR) % mod
            s = (x + sL + (cL * x % mod) + sR + (cR * x % mod)) % mod
            if cL > 0 and cR > 0:
                c = (c + (cL * cR % mod)) % mod
                s = (s + (sL * cR % mod) + (sR * cL % mod) + (cL * cR % mod * x % mod)) % mod
            cnt[x] = (cnt.get(x, 0) + c) % mod
            sm[x] = (sm.get(x, 0) + s) % mod
            ans = (ans + s) % mod
        return ans
