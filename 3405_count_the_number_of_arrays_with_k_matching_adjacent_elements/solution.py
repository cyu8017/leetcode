# LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 1000000007

        def modPow(a: int, e: int) -> int:
            r = 1
            base = ((a % mod) + mod) % mod
            exp = e
            while exp > 0:
                if exp & 1:
                    r = (r * base) % mod
                base = (base * base) % mod
                exp >>= 1
            return r

        def comb(nn: int, kk: int) -> int:
            if kk < 0 or kk > nn:
                return 0
            num = 1
            den = 1
            for i in range(kk):
                num = (num * (nn - i)) % mod
                den = (den * (i + 1)) % mod
            return (num * modPow(den, mod - 2)) % mod

        return comb(n - 1, k) * m % mod * modPow(m - 1, n - 1 - k) % mod
