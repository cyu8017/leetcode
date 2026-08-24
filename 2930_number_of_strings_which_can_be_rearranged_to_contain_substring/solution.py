# LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
# https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/


class Solution:
    def stringCount(self, n: int) -> int:
        if n < 4:
            return 0
        mod = 1000000007

        def modPow(a: int, b: int) -> int:
            res = 1
            a %= mod
            while b > 0:
                if b & 1:
                    res = (res * a) % mod
                a = (a * a) % mod
                b >>= 1
            return res

        return (
            modPow(26, n)
            - (modPow(25, n - 1) * (75 + n))
            + (modPow(24, n - 1) * (72 + 2 * n))
            - (modPow(23, n - 1) * (23 + n))
        ) % mod
