# LeetCode 2183 - Count Array Pairs Divisible by K
# https://leetcode.com/problems/count-array-pairs-divisible-by-k/

from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            while b != 0:
                t = a % b
                a = b
                b = t
            return a

        freq = {}
        ans = 0
        for x in nums:
            g1 = gcd(x, k)
            for g2, cnt in freq.items():
                if (g1 * g2) % k == 0:
                    ans += cnt
            freq[g1] = (freq.get(g1) or 0) + 1
        return ans
