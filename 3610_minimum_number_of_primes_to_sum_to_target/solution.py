# LeetCode 3610 - Minimum Number of Primes to Sum to Target
# https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/


_primes3610 = []


def ensure_primes3610() -> None:
    if _primes3610:
        return
    x = 2
    while len(_primes3610) < 1000:
        is_prime = True
        for p in _primes3610:
            if p * p > x:
                break
            if x % p == 0:
                is_prime = False
                break
        if is_prime:
            _primes3610.append(x)
        x += 1


class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        ensure_primes3610()
        Inf = 2147483647 // 2
        f = [Inf] * (n + 1)
        f[0] = 0
        for pi in range(m):
            x = _primes3610[pi]
            for i in range(x, n + 1):
                if f[i - x] + 1 < f[i]:
                    f[i] = f[i - x] + 1
        return f[n] if f[n] < Inf else -1
