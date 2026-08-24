# LeetCode 3757 - Number of Effective Subsequences
# https://leetcode.com/problems/number-of-effective-subsequences/

from typing import List


class Solution:
    def countEffectiveSubsequences(self, nums: List[int]) -> int:
        def PopCount(x: int) -> int:
            c = 0
            while x != 0:
                c += x & 1
                x >>= 1
            return c

        mod = 1000000007
        allv = 0
        for x in nums:
            allv |= x
        bits = []
        for b in range(20):
            if ((allv >> b) & 1) != 0:
                bits.append(b)
        m = len(bits)
        freq = [0] * (1 << m)
        for x in nums:
            mask = 0
            for i in range(m):
                if ((x >> bits[i]) & 1) != 0:
                    mask |= 1 << i
            freq[mask] += 1
        disjoint = freq[:]
        for b in range(m):
            for mask in range(1 << m):
                if ((mask >> b) & 1) != 0:
                    disjoint[mask] += disjoint[mask ^ (1 << b)]
        pow2 = [0] * (len(nums) + 1)
        pow2[0] = 1
        for i in range(1, len(nums) + 1):
            pow2[i] = pow2[i - 1] * 2 % mod
        ans = 0
        full = (1 << m) - 1
        for s in range(1, full + 1):
            ways = pow2[disjoint[full ^ s]]
            bc = PopCount(s)
            if (bc & 1) != 0:
                ans += ways
                if ans >= mod:
                    ans -= mod
            else:
                ans -= ways
                if ans < 0:
                    ans += mod
        return ans
