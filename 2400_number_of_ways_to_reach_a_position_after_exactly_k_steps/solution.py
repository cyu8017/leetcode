# LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod = 1000000007

        def mod_pow(a: int, e: int) -> int:
            res = 1
            base = a % mod
            while e > 0:
                if e & 1:
                    res = res * base % mod
                base = base * base % mod
                e >>= 1
            return res

        def comb(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            num = den = 1
            for i in range(r):
                num = num * (n - i) % mod
                den = den * (i + 1) % mod
            return num * mod_pow(den, mod - 2) % mod

        diff = abs(endPos - startPos)
        if diff > k or (k - diff) % 2 != 0:
            return 0
        r = (k + diff) // 2
        return comb(k, r)
