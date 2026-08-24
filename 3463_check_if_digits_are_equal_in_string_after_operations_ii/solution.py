# LeetCode 3463 - Check If Digits Are Equal in String After Operations II
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def mod_pow_p(a: int, e: int, p: int) -> int:
            r = 1
            while e > 0:
                if e % 2 == 1:
                    r = r * a % p
                a = a * a % p
                e //= 2
            return r

        def mod_inv_prime(a: int, p: int) -> int:
            return mod_pow_p(a, p - 2, p)

        def binom_mod(n: int, k: int, p: int) -> int:
            if k < 0 or k > n:
                return 0
            num, den = 1, 1
            for i in range(k):
                num = num * (n - i) % p
                den = den * (i + 1) % p
            return num * mod_inv_prime(den, p) % p

        def crt(a1: int, m1: int, a2: int, m2: int) -> int:
            for x in range(m1 * m2):
                if x % m1 == a1 and x % m2 == a2:
                    return x
            return 0

        def binom_mod10(n: int, k: int) -> int:
            return crt(binom_mod(n, k, 2), 2, binom_mod(n, k, 5), 5)

        def combine_digit(offset: int) -> int:
            n = len(s)
            total = 0
            for i in range(n - 1):
                total = (total + binom_mod10(n - 2, i) * (ord(s[i + offset]) - 48)) % 10
            return total

        return combine_digit(0) == combine_digit(1)
