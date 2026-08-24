# LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
# https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/


class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        mod = 1000000007

        def mod_pow(a: int, e: int) -> int:
            r = 1
            base = a % mod
            while e > 0:
                if e & 1:
                    r = (r * base) % mod
                base = (base * base) % mod
                e >>= 1
            return r

        def comb(nn: int, kk: int) -> int:
            if kk < 0 or kk > nn:
                return 0
            num, den = 1, 1
            for i in range(kk):
                num = num * (nn - i) % mod
                den = den * (i + 1) % mod
            return num * mod_pow(den, mod - 2) % mod

        if k < 2:
            return 0
        total_cells = m * n
        pair_choose = comb(total_cells - 2, k - 2)
        sum_dist = 0
        for d in range(1, m):
            sum_dist += d * (m - d) * n * n
        for d in range(1, n):
            sum_dist += d * (n - d) * m * m
        return sum_dist % mod * pair_choose % mod
