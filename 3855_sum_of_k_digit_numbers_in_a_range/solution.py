# LeetCode 3855 - Sum Of K Digit Numbers In A Range
# https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/


class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        def qpow(a: int, n: int, mod: int) -> int:
            a %= mod
            A = a
            N = n
            MOD = mod
            res = 1
            while N > 0:
                if N & 1:
                    res = res * A % MOD
                A = A * A % MOD
                N >>= 1
            return res

        MOD = 1000000007
        n = r - l + 1
        s = ((l + r) * n // 2) % MOD
        part1 = qpow(n % MOD, k - 1, MOD)
        part2 = (qpow(10, k, MOD) - 1 + MOD) % MOD
        inv9 = qpow(9, MOD - 2, MOD)
        ans = s
        ans = ans * part1 % MOD
        ans = ans * part2 % MOD
        ans = ans * inv9 % MOD
        return ans
