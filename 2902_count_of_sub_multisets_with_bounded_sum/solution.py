# LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
# https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

from typing import List


class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        mod = 1000000007
        freq = {}
        total = 0
        for v in nums:
            freq[v] = freq.get(v, 0) + 1
            total += v
        if total < l:
            return 0
        if r > total:
            r = total
        dp = [0] * (r + 1)
        dp[0] = 1
        zeros = freq.get(0, 0)
        freq.pop(0, None)
        for v, c in freq.items():
            ndp = [0] * (r + 1)
            for s in range(r + 1):
                if dp[s] == 0:
                    continue
                k = 0
                while k <= c and s + k * v <= r:
                    ndp[s + k * v] = (ndp[s + k * v] + dp[s]) % mod
                    k += 1
            dp = ndp
        ans = 0
        for s in range(l, r + 1):
            ans = (ans + dp[s]) % mod
        ans = (ans * (zeros + 1)) % mod
        return ans
